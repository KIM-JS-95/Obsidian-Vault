[[0-디자인패턴 MOC.md]] · #spring/design-pattern #kubernetes/behavioral-pattern <!-- moc-nav -->

# 🚀 쿠버네티스 Singleton Service 패턴 — 다중 Pod 환경의 `@Scheduled` 중복 실행 문제

> [[싱글톤_패턴|기존 싱글톤 패턴]]이 "**한 JVM 프로세스 안에서** 인스턴스를 하나만 만드는" 문제라면, 여기서 다루는 건 "**여러 Pod(=여러 JVM 프로세스) 중 하나만** 특정 작업을 수행하게 만드는" 문제다. 이름은 같지만 다른 레벨의 문제.
>
> 쿠버네티스 관점에서 이건 [[../../Kubernetes/01-애플리케이션_설계와_빌드|Structural Pattern(사이드카/앰배서더/어댑터)]]이 아니라 **Behavioral Pattern**으로 분류된다 — 컨테이너를 어떻게 조합하느냐가 아니라, 여러 Pod 복제본이 어떻게 협업/조율하느냐의 문제이기 때문.

## 🌠 문제 상황

Spring Boot 서비스에 `@Scheduled`로 "주기적으로 외부 API를 호출해서 DB에 저장"하는 로직이 있다고 하자. 이 서비스를 쿠버네티스 Deployment로 배포하면서 가용성을 위해 `replicas: 2` 이상으로 띄우면, **각 Pod가 완전히 독립적인 애플리케이션 인스턴스**이기 때문에 정확히 같은 시각에 각 Pod에서 동일한 스케줄이 동시에 실행된다. 결과: 같은 데이터를 여러 Pod가 동시에 insert하면서 PK/unique 제약 위반, 중복 데이터, DB 락 경합 등이 발생.

## 🌠 해결책 3가지

| 방법 | 분류 | 무중단 배포와의 궁합 | 비고 |
|---|---|---|---|
| **K8s CronJob으로 전환** | Behavioral Pattern - *Periodic Job* | 해당 없음 (애초에 상시 실행 워크로드가 아님) | 이 서비스가 스케줄 작업 "전용"일 때 가장 깔끔. API 트래픽도 처리해야 하면 부적합 |
| **분산 락 (ShedLock)** | Behavioral Pattern - *Singleton Service* | 좋음 — 롤링 업데이트 중 신/구 Pod가 공존해도 락으로 하나만 실행 보장 | RDB만 있으면 추가 인프라 없이 구현 가능 |
| **Leader Election** | Behavioral Pattern - *Singleton Service* | 좋음 | k8s `coordination.k8s.io` Lease API 직접 활용. ShedLock보다 구현 복잡도 높음 |

이 서비스가 API 트래픽도 겸해서 Deployment로 항상 여러 Pod를 띄워야 하고, 무중단 배포(롤링 업데이트) 중에도 스케줄이 끊기거나 중복되면 안 된다면 → **ShedLock(분산 락)** 이 실무에서 가장 많이 쓰이는 선택.

## 🌠 ShedLock 구현

**의존성**
```groovy
implementation 'net.javacrumbs.shedlock:shedlock-spring:5.16.0'
implementation 'net.javacrumbs.shedlock:shedlock-provider-jdbc-template:5.16.0'
```

**락 테이블** — ShedLock은 락 상태를 이 테이블 하나로 관리한다. `name`당 한 행만 존재하고, 여러 Pod가 동시에 이 행을 UPDATE하려 해도 DB 자체의 원자성(row lock)으로 딱 하나만 성공한다.

```sql
CREATE TABLE shedlock (
    name       VARCHAR(64) NOT NULL,
    lock_until TIMESTAMP(3) NOT NULL,
    locked_at  TIMESTAMP(3) NOT NULL,
    locked_by  VARCHAR(255) NOT NULL,
    PRIMARY KEY (name)
);
```

**설정**
```java
@Configuration
@EnableScheduling
@EnableSchedulerLock(defaultLockAtMostFor = "10m")
public class SchedulerConfig {

    @Bean
    public LockProvider lockProvider(DataSource dataSource) {
        return new JdbcTemplateLockProvider(
            JdbcTemplateLockProvider.Configuration.builder()
                .withJdbcTemplate(new JdbcTemplate(dataSource))
                .usingDbTime()   // ⚠️ Pod마다 시스템 시계가 미세하게 다를 수 있으니 DB 시간 기준으로 통일
                .build()
        );
    }
}
```

**사용**
```java
@Scheduled(cron = "0 * * * * *")   // 매 1분
@SchedulerLock(
    name = "collectApiData",
    lockAtLeastFor = "50s",   // 최소 유지 시간 — Pod 간 시계 오차로 인한 중복 실행 방지
    lockAtMostFor = "5m"       // 최대 유지 시간 — Pod가 작업 중 죽어도 다음 스케줄이 영영 막히지 않게 하는 안전장치
)
public void collectAndSaveData() {
    // API 호출 + DB insert 로직
}
```

## 🌠 흔한 함정

1. **자기 클래스 내부 호출 금지**: `@SchedulerLock`은 Spring AOP 프록시로 동작한다. 같은 클래스 안의 다른 메서드가 이 메서드를 직접 호출(self-invocation)하면 프록시를 거치지 않아 락이 걸리지 않는다. 반드시 `@Scheduled`가 붙은 진입점 메서드 자체에 적용해야 한다.
2. **`lockAtLeastFor`를 너무 짧게(또는 0으로) 두면 안 됨**: 작업이 아주 빨리 끝나버리면, 시계가 살짝 빠른 다른 Pod가 그 직후 같은 스케줄 시점에 또 실행해버릴 수 있다.
3. **롤링 업데이트 중 이점**: 신/구 버전 Pod가 잠깐 공존하는 배포 전환 구간에도, 락을 가진 인스턴스 하나만 스케줄을 실행하므로 중복 insert나 스케줄 누락 없이 자연스럽게 넘어간다. CronJob은 이런 배포 전환 시나리오 자체가 없어 이 장점과 무관하다.

## ❓ 확인 질문
1. `lockAtMostFor`를 너무 짧게 잡으면(예: 실제 작업이 3분 걸리는데 1분으로 설정) 어떤 문제가 생길까?
2. 이 서비스를 CronJob으로 바꾸면 `@SchedulerLock`이 여전히 필요할까?

## 🧾 Reference
- [ShedLock GitHub](https://github.com/lukas-krecan/ShedLock)
- [[../../Kubernetes/01-애플리케이션_설계와_빌드|Kubernetes: 애플리케이션 설계와 빌드 (Structural Pattern)]]
- [[싱글톤_패턴|기존 OOP 싱글톤 패턴 (JVM 레벨)]]

# 스프링에서 스레드 동작 방식

스프링 프레임워크는 기본적으로 `싱글톤 스코프의 빈`을 사용하며, 멀티스레드 환경에서도 안전하게 동작하도록 설계되었다.

## 싱글톤 스코프 빈(Singleton Scope Bean)

스프링 컨테이너에서 기본적으로 관리되는 빈의 스코프 중 하나로, Application Context 내에서 단 하나의 인스턴스만 생성되어 모든 요청에서 공유되는 빈을 의미한다.

### 특징

- **단일 인스턴스**:  
    스프링 컨테이너가 애플리케이션 시작 시 메모리 사용량을 줄이고 빈 생성 비용을 최소화하기 위해 싱글톤 스코프 빈의 인스턴스를 한 번 생성하고, 이후 모든 요청에서 동일한 인스턴스를 반환한다.

- **상태 관리 주의**:  
    여러 스레드가 동일한 인스턴스를 공유하기 때문에, 빈이 상태를 가지는 경우(thread-safe하지 않은 경우) 멀티스레드 환경에서 동기화 문제가 발생할 수 있다. 따라서 싱글톤 스코프 빈은 **무상태(stateless)**로 설계하는 것이 권장된다.

### 싱글톤 스코프의 장점

- **효율성**: 빈을 한 번만 생성하므로 메모리와 리소스를 절약한다.
- **관리 용이성**: 애플리케이션 전역에서 동일한 인스턴스를 사용하므로 관리가 간단하다.

### 주의사항

- 상태를 가지는 필드(예: 인스턴스 변수)를 포함하면, 멀티스레드 환경에서 데이터 충돌이 발생할 수 있다.
- 상태를 유지해야 한다면, 프로토타입 스코프나 `ThreadLocal`을 사용하는 것이 적합하다.


## 1. 스레드 안전성

스프링 빈은 기본적으로 싱글톤 스코프를 가지므로, 여러 스레드가 동시에 동일한 빈 인스턴스에 접근할 수 있다. 따라서 상태를 가지는 빈은 멀티스레드 환경에서 스레드 안전하지 않을 수 있다. 이를 해결하기 위해 다음과 같은 방법을 사용할 수 있다:

- **Stateless 빈 사용**: 상태를 가지지 않는 빈을 설계한다.
- **ThreadLocal 사용**: 스레드별로 데이터를 저장한다.
- **프로토타입 스코프 빈 사용**: 요청마다 새로운 빈 인스턴스를 생성한다.
- **동기화 처리**: 상태를 가지는 경우, 동기화(synchronization)를 통해 스레드 안전성을 보장한다.

## 2. @Async를 통한 비동기 처리

스프링은 `@Async` 어노테이션을 사용하여 비동기 메서드를 실행할 수 있다. 이를 통해 별도의 스레드에서 작업을 처리할 수 있다.

```java
@Service
public class AsyncService {
        @Async
        public void executeAsyncTask() {
                System.out.println("비동기 작업 실행 중...");
        }
}
```

- `@EnableAsync` 어노테이션을 추가하여 비동기 처리를 활성화해야 한다.
- 기본적으로 스프링은 `SimpleAsyncTaskExecutor`를 사용하지만, `TaskExecutor`를 커스터마이징하여 스레드 풀을 설정할 수 있다.

## 3. 스레드 풀 설정

스레드 풀은 스레드 생성 비용을 줄이고, 시스템 리소스를 효율적으로 사용할 수 있도록 도와준다. 스프링에서 스레드 풀을 설정하려면 `ThreadPoolTaskExecutor`를 사용한다.

```java
@Configuration
@EnableAsync
public class AsyncConfig {
        @Bean
        public Executor taskExecutor() {
                ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
                executor.setCorePoolSize(5);
                executor.setMaxPoolSize(10);
                executor.setQueueCapacity(25);
                executor.setThreadNamePrefix("AsyncExecutor-");
                executor.initialize();
                return executor;
        }
}
```

## 4. 트랜잭션과 스레드

스프링의 트랜잭션은 기본적으로 `ThreadLocal`을 사용하여 트랜잭션 컨텍스트를 관리한다. 따라서 동일한 스레드 내에서만 트랜잭션이 전파된다. 비동기 작업이나 다른 스레드에서 트랜잭션을 사용하려면 별도의 설정이 필요하다.

## 5. 주의사항

- 멀티스레드 환경에서 상태를 가지는 빈은 동기화(synchronization) 처리가 필요하다.

- 비동기 작업에서 예외 처리를 위해 `AsyncUncaughtExceptionHandler`를 구현할 수 있다.
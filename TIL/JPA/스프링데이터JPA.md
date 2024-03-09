# 🍃 JPA를 위한 Spring Data

## Spring Data?

### Features

- 강력한 리포지토리 및 사용자 지정 개체 매핑 추상화입니다.

- 리포지토리 메서드 이름에서 동적 쿼리를 파생합니다.

- 기본 속성을 제공하는 구현 도메인 기본 클래스입니다.

- 투명 감사(생성, 최종 변경)를 지원합니다.

- 사용자 정의 리포지토리 코드를 통합할 수 있습니다.

- JavaConfig 및 사용자 지정 XML 네임스페이스를 통한 쉬운 스프링 통합입니다.

- Spring MVC 컨트롤러와 고급 통합됩니다.

- 교차 스토어 지속성에 대한 실험적 지원을 제공합니다.


- 출처 : [Spring 공식 페이지](https://spring.io/)


## JPA의 구원자
이전까지 JPA에서 제공된 객체쿼리는 `String` 타입으로 JPA에서 SQL 쿼리로 변환 하여 전달하는 방식이라면
`SpringData JPA`는 스프링 프레임워크에서 JPA를 편리하게 상용할 수 있도록 지원하는 인터페이스이다.

즉, `CRUD`를 처리하기 위한 공통 인터페이스를 제공해 주는 것으로 반복적인 개발 방식에서 벗어 날 수 있는 것이다.

```java
public interface MemberRepository extends JpaRepository<Member, Long>{
    Member findByUsername(String name);
}
```

**물론 Spring JPA 또한 `Hibernate`로 부터 개발된 인터페이스로서 실행시 JPQL로 번역되어 SQL에 전달 되어진다.**   

## 쿼리 메소드
스프링 데이터가 가지는 장점은 `쿼리 메소드`를 지원하는 것이며 쿼리 메소드는 3가지의 기능을 가진다.

- 메소드 이름으로 생성
- JPA NamedQuery 호출
- @Query를 사용하여 직접 정의

**자세한건 책을 찾아 보자**
# 🍃 JPA를 위한 Spring Data

## Spring Data?
    
    Spring Data’s mission is to provide a familiar and consistent, 
    Spring-based programming model for data access while still retaining the special traits of the underlying data store.
    
    It makes it easy to use data access technologies, relational and non-relational databases, map-reduce frameworks, 
    and cloud-based data services. This is an umbrella project which contains many subprojects that are specific to a given database. 
    
    The projects are developed by working together with many of the companies and developers that are behind these exciting technologies.

    Spring Data의 사명은 친숙하고 일관된 서비스를 제공하는 것입니다.
    기본 데이터 저장소의 특수 특성을 유지하면서 데이터 액세스를 위한 스프링 기반 프로그래밍 모델입니다.
    
    데이터 액세스 기술, 관계형 및 비관계형 데이터베이스, 지도 축소 프레임워크를 쉽게 사용할 수 있습니다.
    클라우드 기반 데이터 서비스를 제공합니다. 이것은 지정된 데이터베이스와 관련된 많은 하위 프로젝트를 포함하는 상위 프로젝트입니다.
    
    이 프로젝트는 이러한 흥미로운 기술의 배후에 있는 많은 회사 및 개발자들과 협력하여 개발됩니다.

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
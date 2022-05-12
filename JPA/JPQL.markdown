# JPQL

## 특징
- `JPQL`은 엔티티 객체 중심의 객체지향 쿼리 언어이다.
- `JPQL`은 SQL을 추상화해서 특정 데이터베이스 SQL에 의존하지 않는다.
- `JPQL` 쿼리는 커밋과 동시에 SQL로 재해석되어 전달하게 된다.

## 기본 문법

- 대소문자 구분
- 엔티티 이름을
  - 클래스 이름이 아닌 `@Entity(name = "Member")` 으로 지정된 엔티티 이름을 사용한다.
- 별칭은 필수


## 알고 들어가자!
### 파라미터

JDBC는 위치 기준 파라미터 바인딩만 지원하지만 JPQL은 `이름 기준 파라미터 바인딩` 과 `위치 기준 파라미터`를 지원한다.

- JDBC 쿼리 예시
``` java
// SQL 선언
        StringBuffer sql = new StringBuffer();
        sql.append("SELECT * FROM Member where username = ?");
// 파라미터 바인딩
        preparedStatement = con.prepareStatement(sql.toString());
        preparedStatement.setString(1, "kim");
```

- JPQL 쿼리 예시 (이름 기준)
```java
String usernameParam = "SELECT m FROM Member AS m where m.username = :username";
query.setParameter("username", "kim")
```


- JPQL 쿼리 예시 (위치 기준)
  - 위치 기준 파라미터의 경우 위치는 항상 `1`부터 시작된다.
```java
String usernameParam = "SELECT m FROM Member AS m where m.username = ?1";
query.setParameter(1, "kim")
```

> 어떤 파라미터가 더 좋을까? 꼭 사용해야할까?
> 
> 파라미터의 경우 이름을 기준으로 사용하는 것이 더욱 직관적이며 명확하다.
> 
> 만일 쿼리 내부에 직접적으로 변수를 합친다면 `SQL인젝션 공격`에 당할 수 있으며 
> 
> 파라미터 값이 달라도 쿼리로 인식하여 JPQL을 SQL로 파싱한 결과를 재사용할 수 있어 전체 성능이 향상될 수 있다. 

### TypeQuery, Query
객체를 반환받기 위해서는 반환 타입을 명시 해줘야한다.
그러나 항상 반환받을 타입을 알수 있는 것은 아니다.

그렇기에 `TypeQuery`, `Query` 두 가지로 구분하여 사용한다.
- TypeQuery
  - 반환 받을 타입을 명확하게 지정할 수 있을 경우 사용

```
TypeQuery<Member> q = em.createQuery("SELECT m FROM Member m", Member.class);
```
- Query
  - 반환 받을 타임을 지정할 수 없을 경우 사용 (반환 받을 데이터 타입이 두 가지 이상일 경우)
```
Query q = em.createQuery("SELECT m.username, m.age FROM Member m", Member.class);
```

## 페치 조인
`JPQL`에서 성능 최적화를 위해 제공하는 기능으로 

연관된 엔티티나 컬렉션을 한 번에 같이 조회하는 기능이며 `join fetch` 명령어로 사용할 수 있다.

- fetch 조인은 별칭을 사용할 수 없다.
- JPQL은 일반 조인과 다르게 SELECT 절에 지정한 엔티티만 조회한다.
- 둘 이상의 컬렉션을 페치할 수 없다.
- 컬렉션을 페치 조인하면 페이징 API를 사용할 수 없다.

```
select m from Member join fetch m.team
```

### @OneToMany(fetch = "FetchType.Lazy") 와 페치 조인의 차이

페치 조인을 사용하면 SQL 한 번으로 연관된 엔티티들을 함께 조횔할 수 있어서 SQL 호출 횟수를 줄여 성능을 최적화 할 수 있다.

목적성을 본다면 `fetch = "FetchType.Lazy"`와 같다 생각하지만 애플리케이션 전체에 영향을 준다는 점에서 `글로벌 로딩 전략`으로 본다.

또한 `페치 조인`은 글로벌 로딩 전략 보다 우선시 된다.

정리하자면 최적회를 위해 `글로벌 로딩 전략`을 사용한다면 속도 면에서는 개성 될테지만 성능명에서는 효율성이 떨어질 수 있다.

따라서 엔티티가 가지는 `글로벌 로딩 전략`을 `Lazy`를 사용하며 필요시에 `페치 전략`을 사용하는 것이 효과적이다.





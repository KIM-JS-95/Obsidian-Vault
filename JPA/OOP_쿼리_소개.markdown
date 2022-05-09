# 객체지향 쿼리의 필요성

이전 까지 단순 조회는 `find` `findAll` 수준의 단순 조회 였지만 조건을 부여하기에는 한계가 있었다.

이러한 문제로 들장한 개념이 `객체지향 쿼리` 이다.

## JPQL

단순 SQL이 DB 테이블을 대상으로 하는 데이터 중심 쿼리라면 JPQL은 엔티티 객체를 대상으로 하는 객체지향 쿼리이다.

JPQL을 사용하면 JPA는 해당 쿼리를 분석하여 SQL쿼리를 생성하여 SQL을 조회한다.

- 테이블이 아닌 객체를 대상으로 검색하는 객체지향 쿼리이다.
- **SQL을 추상화해서 특정 데이터 베이스 SQL에 의존하지 않는다.** (중요)

```mysql-psql
String jpql = "select m from Member as m where m.username = 'kim';"
List<Member> resultList = 
                        em.createQuery(jpql, Member.class).getResultList();
```

### JPQL의 문제점

```mysql-psql
String jpql = "select m from Membeee;"
List<Member> resultList = 
                        em.createQuery(jpql, Member.class).getResultList();
```

문자 기반의 쿼리의 단점은 쿼리문에 문제가 발생해도 컴파일과 서버 배포에는 문제가 없지만 

**쿼리가 실행되는 런타임 시점에 오루가 발생한다는 점이다.**

## Criteria

`JPQL`이 문자열 방식의 쿼리라면 `Criteria`는 <u>코드 방식의 쿼리문</u>이다.

- 컴파일 시점에 오류를 발견할 수 있다.
- IDE를 사용하면 코드 자동완성을 지원한다.
- 동적 쿼리를 작성하기 편하다.


```mysql-psql
// 사용준비
CriteriaBuilder cb = em.getCriteriaBuilder();
CriteriaQuery<Member> query = cb.createQuery(Member.class);

// 루트 클래스(조회를 시작할 클래스)
Root<Member> m = query.from(Member.class)

// 쿼리생성
CriteriaQuery<Member> cq =
                    query.select(m).where(cb.equal(m.get("username"), "kim"));

List<Member> resultList = em.createQuery(cq).getResultList();
```

### Criteria 문제점
- 쿼리를 생성하기 위해 준비해야하는 과정이 많다.
- 불편한 사용과 함께 가독성이 떨어진다.


## QueryDSL

상대적으로 `Criteria` 보다 단순하다.

```mysql-psql
// 준비
JPAQuery query = new JPAQuery(em);
QMember member = QMember.member;

// 쿼리, 결과 조회
List<Member> members =
                query.from(member)
                .where(emember.username.eq("kim))
                .list(member);

```

## Native 쿼리

객체지향 쿼리를 사용해도 쿼리의 모든 기능을 대체할 수는 없다.

때문에 JPA는 `SQL쿼리`를 직접 사용할 수 있도록 지원한다.

### Native 문제점
쿼리를 직접 작성할 수 있는 만큼 **특정 데이터 베이스에 의존하는 SQL을 작성해야 한다는 점이다.**

즉, DB의 종류가 바뀌면 해당 쿼리문 전체를 바꿔야 하는 문제가 나타나는 것이다.

## JDBC 직접 사용, 마이바티스 같은 SQL 매퍼 프레임워크 사용

JDBC 커넥션에 직접 접근하고자 한다면 JPA 구현체가 제공하는 방법을 사용해야 한다.

```java
Session session = entityManager.unwrap(Session.class);

session.dowork(new Work() {
    @Override
    public void execute(Connection connection) throws SQLException {
        // DO work ...     
        }
});
```

JDBC나 Mybatis를 JPA와 함께 사용하면 영속성 컨텍스트를 적절한 시점에 강제로 플러시해야 한다.

`JDBC`와 `SQL Mapper`는 JPA를 우회에서 데이터 베이스에 접근하기 때문에 `commit` 을 인식하지 못한다.

**즉, 데이터 베이스의 무결성을 보장하지 못한다는 점이다.**

이러한 문제는 SQL을 실행하기 직전에 영속성 컨텍스트를 수동을 플러시해서 데이터 베이스와 영속성 컨텍스트를 동기화 하면 된다.

### 스프링 프레임워크에서 문제를 해결하다.

Spring Framework 의 AOP를 활용한다면 DB에 접근하는 메소드를 호출할 떄 마다 영송석 컨텍스트를 플러시 하면 
`무결성` 문제를 해결할 수 있다.


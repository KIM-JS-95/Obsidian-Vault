---
layout: post 
title:  "객체지향 쿼리 JPQL"
date:   2021-06-21 12:05:21 +0800 
tags: JPA SPRING JPQL 
color: rgb(154,133,255)
subtitle: 'JPQL'
--- 

## 객체지향 쿼리 JPQL

### SQL vs JPQL

* 테이블이 아닌 객체를 대상으로 검색하는 객체지향 쿼리
* <u>SQL을 추상화</u>해서 특정 DB SQL에 의존하지 않는다.

| 구분 | SQL | JPQL |
|:---:|:---:|:---:|
| 대상 | DATA | 객체 |
| 쿼리 형태 | DATA 중심의 쿼리 | 객체 중심의 쿼리 |

### JPQL(정적 쿼리) ?

JPQL(Java Persistence Query Language)은 객체를 조회하는 객체지향 쿼리이다. 객체 중심의 문법인 만큼 특정 DB에 의존하지 않는다. 엔티티 조회, 묵시적 조인, 다형성 지원으로 SQL
보다 간결하다.
> 다형성(polymorphism) ?
>
> 하나의 객체가 여러 가지 타입을 가질 수 있는 것을 의미합니다. 자바에서는 이러한 다형성을 부모 클래스 타입의 참조 변수로 자식 클래스 타입의 인스턴스를 참조할 수 있도록 하여 구현
>
>다형성은 상속, 추상화와 더불어 객체 지향 프로그래밍을 구성하는 중요한 특징 중 하나입니다.

### JPQL 쿼리와 SQL 쿼리 차이

#### JPQL(문자형태)

* select_문 ::= select_절 from_절 where_절 groupby_절 having_절 orderby_절

* update_문 ::= update_절 where_절

* delete_문 ::= delete_절 where_절

SELECT, UPDATE, DELETE 문 사용이 가능하지만 INSERT문은 없다.

#### SQL(문자형태)

* SELECT m FROM Member AS m WHERE m.username = 'leveloper'

#### 차이점

1. 대소문자 구분

엔티티와 속성은 대소문자를 구분한다. 예를 들어, Member, username은 대소문자를 구분해줘야 한다. 반면에 SELECT, FROM, WHERE 같은 JPQL 키워드는 대소문자를 구분하지 않아도 된다.

2. 엔티티 이름

JPQL에서 사용한 Member는 클래스 명이 아니라 엔티티 명이다. 엔티티명은 @Entity(name="abc")로 지정할 수 있다. 엔티티 명을 지정하지 않으면 클래스 명을 기본값으로 사용한다.

3. 별칭은 필수

Member AS m을 보면 Member에 m이라는 별칭을 주었다. JPQL은 별칭을 필수로 사용해야 한다. AS를 생략해서 Member m처럼 사용해도 된다.

#### SQL, JPQL의 문제점
* 문자열 형태의 SQL, JPQL

* 컴파일 시점에 알 수 있는 방법이 없다.

* 해당 로직 실행 전까지 작동여부 확인을 할 수 없다. (쿼리 작동시 오류 확인 가능)

---

### Other 쿼리

#### 1. Criteria 쿼리(코드형태)

Criteria는 JPQL을 생성하는 빌더 클래스이며 <u>프로그래밍 코드로 JPQL을 작성할 수 있다는 장점이있다.</u>
문제는 JPQL에서 쿼리를 작성하여 배포까지 가능해도 <u>해당 쿼리가 런타임 시점에 오류가 발생</u> 한다는 점이다. 이것은 문자기반 쿼리의 단점이다.

```bash
// 사용준비
CriteriaBuilder builder = em.getCriteriaBuilder(); --> 1
CriteriaQuery<MemberJPQL> query = builder.createQuery(MemberJPQL.class); --> 2

// FROM 절을 생성한다. 반환된 값 m은  Criteria에서 사용하는 특별한 별칭이다. m을 조회의 시작점이라는 의미로 쿼리 루트(Root)라고 한다.
Root<MemberJPQL> m = query.from(MemberJPQL.class); --> 3

// SELECT 절을 생성한다. 
query.select(m).distinct(true); --> 4
TypedQuery<MemberJPQL> typeQuery = em.createQuery(query);
List<MemberJPQL> members = typeQuery.getResultList();
```

> Criteria 장점
> * 컴파일 시점에 오류를 발견할 수 있다.
> * 코드 자동완성 지원
> * 동적 쿼리를 작성하기 편하다.

> Criteria 단점
> * 런타임 시점에 오류가 발생 가능성
> * 복잡한 사용 방식 가독성 떨어짐

---

#### 2. QueryDSL(코드형태)

Criteria 쿼리와 동일하게 JPQL 빌더 역할을 가지며 단순하고 사용하기 편리하다. 단 비표준화 형태의 쿼리

```bash
// 준비
JPAQuery query = new JPAQuery(em);
QMember member - QMember.member;

// 쿼리, 결과조회
List<Member> list = 
    query.selectFrom(m)
         .where(m.age.gt(18))
         .orderBy(m.name.desc())
        .limit(10)
         .offset(10)
         .fetch();
        
// 페이징  limit, offset도 그냥 넣어줄 수 있다.
```

> QueryDSL 장점
> * 문자가 아닌 코드로 작성
> * 컴파일 시점에 문법 오류를 발견
> * 코드 자동완성
> * 단순하고 쉽다. 코드 모양이 JPQL과 거의 유사
> * 동적 쿼리

> QueryDSL 단점
> * QueryDSL은 Entity 클래스를 기반으로 QueryDSL 쿼리 전용 클래스를 만들어야 하는 단점

---

#### 3. 네이티브 SQL(문자형태)
JPA는 SQL이 지원하는 대부분의 문법과 SQL 함수들을 지원하지만 <u>특정 데이터베이스에 종속적인 기능은
잘 지원하지 않는다.</u> 만일 특정 DB를 조회할 경우 JPA는 SQL을 직접 사용할 수 있는 기능을 지원하며
이를 <u>네이티브 SQL이라고 한다.</u>

```bash
// 문자 생성
String sql = "SELETE ID, AGE, TEAM-ID, NAME FROM MEMBER, WHERE NAME = `kim`";

// 쿼리 , 결과 조회
List<Member> resultList = em.createNativeQuert(sql, Member.class).getResultList(); 
```

> 네이티브 SQL 장점
> * 특정 DB에 접근을 위한 JPA의 대체로 사용할 수 있다.

> 네이티브 SQL 단점
> * 특정 DB에 의존하는 만큼 DB가 변경될 경우 네이티브 SQL 쿼리도 수정해야한다.


### 쿼리 객체의 반환
작성한 JPQL을 실행 하려면 쿼리 객체를 만들어야 하며 객체는 TypeQuery, Query가 있으며 반환 타입의 명확한 지정의 유무에 따라
달리 사용할 수 있다. (명확: TypeQuery / 불명확: Query)

```bash
// 문자 생성
TypeQuery<Member> query = em.createQuery("SELETE m.username, m.age from Member m");
// 쿼리 , 결과 조회
List resultList =query.getResultList();

for(Member member : resultList){
  System.out.println("member");
} 
```

```bash
// 문자 생성
Query query = em.createQuery("SELETE m.username, m.age from Member m");
// 쿼리 , 결과 조회
List resultList =query.getResultList();

for(Object o : resultList){
  Object[] result = (Object[]) o;  //결과가 둘 이상이면 Object[] 반환
  System.out.println(result[0]);
  System.out.println(result[1]);
} 
```

### Reference
[!QueryDSL](https://ict-nroo.tistory.com/117)
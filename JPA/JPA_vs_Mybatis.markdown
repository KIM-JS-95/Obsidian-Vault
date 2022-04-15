---
layout: post
title:  "JPA vs Mybatis 차이"
date:   2022-01-29 12:05:21 +0800
tags: Spring Interview
color: rgb(154,133,255)
subtitle: 기술면접
--- 

### ORM (Object - Relational - Mapping)
객체와 DB를 매핑하는 기술로 객체와 테이블을 <u>자동으로 매핑해서 패러다임의 불일치 문제를 자동으로 해결</u>해준다.
SQL 중심의 매핑이 아닌 자바 클래스 위주의 매핑이다.

####모든 자동 매핑이 ORM은 아니다!
객체와 DB를 자동으로 매핑해준다는 점에서 결국 `Mybatis` 또한 ORM에 속할지도 모르지만 직접 쿼리를 작성한다는 점에서
<u>SQL 중심의 개발 방식</u>에 가깝기 때문에 ORM 진영에는 반대에 있다고 할 수 있다.

### 🚀 Hibernate

`Hibernate`는 JPA의 인터페이스를 구현한 구현체이다.

JPA와 Hibernate는 마치 자바의 `interface`와 해당 `interface를 구현한 class`와 같은 관계이다.


### 🚀 JPA(Java Persistent API)

JPA는 자바 진영의 ORM 기술 표준이며 `관계형 데이터베이스`와 `자바 객체`를 매핑하기 위한 `EntityManager` 
인터페이스를 제공한다.

#### 장점
+ CRUD 쿼리를 자동으로 생성해준다.
+ DB 종류에 상관없이 사용 가능하다.
+ Entity에 속성만 추가해준다면 쿼리를 건들 필요가 없다.

#### 단점
+ 상대적으로 학습이 어렵다.
+ 복잡한 쿼리 작성이 어렵다.
+ 동적 쿼리 같은 복잡한 쿼리를 처리하는 것이 어려우므로 QueryDSL을 함께 이용한다.

#### 🚀 Spring Data JPA

JPA는 `인터페이스` 다시말해 명세서이며 RDB 환경에서 DB를 어떻게 처리를 해야하는지에 대한 하나의 방법론이다.

이 인터페이스를 <u>유저가 쉽게 다룰 수 있도록 만들어 놓은 모듈</u>이 `Spring Data JPA`가 되는 것이다.
기존 `EntityManager`에서 벗어나 `Repository` 인터페이스를 사용하여 Spring Framework의 규칙대로 메소드를 입력하여 사용하며
입력된 메소드는 SQL문법에 맞추어 구현체로 만들어 `Bean`으로 만들어 컨테이너에 저장되게 된다.

![](https://suhwan.dev/images/jpa_hibernate_repository/overall_design.png)

### 🚀 Mybatis

기존의 JDBC에서 볼 수 있는 반복적인 코드 그리고 직접적인 DB관리를 개선하기위해 등장한 프레임워크이다.

Mybatis는 기존 JDBC의 문제점을 개선한 객체지향 언어인 자바의 관계형 데이터베이스 프로그래밍을
 좀 더 쉽게 할 수 있게 도와주는 개발 프레임워크이며
Mybatis는 JDBC로 처리하는 상당 부분의 코드와 파라미터 설정 및 결과를 자동 매핑을 해준다.


#### 장점
+ 학습이 쉽다.
+ 소스코드와 SQL을 분리할 수 있다.

#### 단점
+ 반복적인 작업이 반복된다.
+ DB 변경시 혹은 스키마 변경시 로직도 같이 변경해 주어야한다.



### JPA vs Mybatis

1. 쿼리지향 vs 객체지향 

JDBC의 문제점을 보완한 `Mybatis`는 반복적인 쿼리 작성, 수동적인 테이블 객체 관리의 어려움을 개선해 주었지만
`xml파일`을 통해 쿼리를 직접 작성해 주어야하는 관점에서 SQL에 직접 쿼리를 보내는 쿼리지향이기 때문에 사용하기가 쉽다. 

2. ORM 사용의 차이

`Mybatis`가 DB과 연결되기 위해서는 `XML 파일`을 사용하여 연동해야하며 해당 파일에는 로직에 필요한 `SQL쿼리`가 작성되어진다.
때문에 ORM보다는 SQL_Mapper에 가까문 명세서로 볼 수 있다.

그러나 JPA의 경우 파일이 아닌 `.Class`를 작성하여 테이블 객체와 연결하기 때문에 스키마 / DB 프로그램이 바뀌어도 직접 변경 할 필요가 없다.
이는 JPA 인터페이스를 기반으로 모든 작업을 자동으로 처리해주는 이점이 있기 때문이다.
이러한 결과로 `JPA`가 `Mybatis` 보다는 비즈니스 로직에 집중해서 개발 할 수 있다. 

### 🧾Reference
[MyBatis와 JPA의 차이, MyBatis보다 JPA를 사용해야 하는 이유](https://mangkyu.tistory.com/20)
[ORM이란](https://gmlwjd9405.github.io/2019/02/01/orm.html)
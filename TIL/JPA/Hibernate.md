[[0-JPA MOC.md]] · #jpa <!-- moc-nav -->

## 🚀 Hibernate

`Hibernate`는 JPA의 인터페이스를 구현한 구현체이다.

JPA와 Hibernate는 마치 자바의 `interface`와 해당 `interface를 구현한 class`와 같은 관계이다.


## 🚀 JPA(Java Persistent API)

JPA는 자바 진영의 ORM 기술 표준이며 `관계형 데이터베이스`와 `자바 객체`를 매핑하기 위한 `EntityManager` 
인터페이스를 제공한다.

### 🌠 장점
+ CRUD 쿼리를 자동으로 생성해준다.
+ DB 종류에 상관없이 사용 가능하다.
+ Entity에 속성만 추가해준다면 쿼리를 건들 필요가 없다.

### 🌠 단점
+ 상대적으로 학습이 어렵다.
+ 복잡한 쿼리 작성이 어렵다.
+ 동적 쿼리 같은 복잡한 쿼리를 처리하는 것이 어려우므로 QueryDSL을 함께 이용한다.


![](https://ultrakain.gitbooks.io/jpa/content/chapter1/images/JPA_search.png)


## 🚀 Spring Data JPA

JPA는 `인터페이스` 다시말해 명세서이며 RDB 환경에서 DB를 어떻게 처리를 해야하는지에 대한 하나의 방법론이다.

이 인터페이스를 <u>유저가 쉽게 다룰 수 있도록 만들어 놓은 모듈</u>이 `Spring Data JPA`가 되는 것이다.
기존 `EntityManager`에서 벗어나 `Repository` 인터페이스를 사용하여 Spring Framework의 규칙대로 메소드를 입력하여 사용하며
입력된 메소드는 SQL문법에 맞추어 구현체로 만들어 `Bean`으로 만들어 컨테이너에 저장되게 된다.

![](https://suhwan.dev/images/jpa_hibernate_repository/overall_design.png)



## 🧾 Reference
[MyBatis와 JPA의 차이, MyBatis보다 JPA를 사용해야 하는 이유](https://mangkyu.tistory.com/20)
[ORM이란](https://gmlwjd9405.github.io/2019/02/01/orm.html)
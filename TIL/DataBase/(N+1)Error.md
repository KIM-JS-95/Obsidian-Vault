
# Background
## 준영속 상태와 지연로딩
스프링 컨테이너는 트랜잭션 범위의 영속성 컨텍스트 전략을 기본으로 사용한다.
즉, 트랜잭션 범위와 영속성 컨텍스트의 생존 범위가 같다는 뜻이다. 그리고
트랜잭션은 보통 서비스 계층에서 시작하므로 서비스 계층이 끝나는 시점에 트랜잭션이 종료되면서 영속성 컨텍스트로 함께 종료된다.

```java
@Entity
public class order{
    @Id @GeneratorValue
    private Long id;
    
    @ManyToOne(fetch = FetchType.LAZY)
    private Member member;
}
```

컨테이너 환경의 기본 전략인 트랜잭션 범위의 영속성 컨택스트 전략을 사용하면 트랜잭션이 없는 프래젠테이션 계층에서 엔티티는 준영속 상태다.
따라서 감지와 지연 로딩이 동작하지 않는다.

```java
class OrderController{
    public String view(Long orderId){
        Order order = orderService.findOne(orderId);
        Member member = order.getMember();
        member.getName(); // 지연로딩 시 예외 발생 
    }
}
```

* 준영속 상태와 변경 감지
**변경감지기능**은 영속성  컨텍스트가 살아있는 서비스 계틍까지만 동작하고 영속성 컨텍스트가 종료된 프레젠테이션 계층에서는 동작하지 않는다.
  
    (보통은 비즈니스 로직을 수행하면서 발생)
반대로 **변경감지기능**이 프레젠테이션 계층에서 동작하게 되면 책인이 모호해지고 유지보수가 어려워진다. 
  
* 준영속 상태외 지연로딩
준영속 상태의 가장 큰 문제점은 <u>지연로딩이 동작하지 않는다는 점이다.</u> 
  * 해결방법
    1. 뷰가 필요한 엔티티를 미리 로딩해두는 방법
    2. OSIV를 사용해서 엔티티를 항상 영속 상태로 유지하는 방법
    
```
뷰가 필요한 엔티티를 미리 로딩 하는 방법
1. 글로벌 페치 전략 수정
2. JPQL 페치 조인
3. 강제 초기화
```

## What is (N+1) Error?
<u>글로벌 페치 전략에 즉시 로딩 시의 단점</u>중 하나로 조회한 order 엔티티가 10개면 member를 조회하는 SQL도 10번 실행하는 조회 중복 과정으로
조회 성능에 치명적 오류이므로 최적화가 필요하다. 주로 즉시로딩 / 지연로딩 의 단점으로 나타난다.

### 즉시 로딩
특정 회원 하나를 조회하면 <u>즉시로딩</u>으로 설정한 주문정보도 함께 조회한다. 즉 두 엔티티를 따로 두번 조회한 것이 아닌 한꺼번에 함께 조회한다.
여기서 JPQL을 실행하면 JPA는 이것을 분석하여 SQL을 생성하는 과정에서 주문 엔티티가 즉시로딩으로 설정되어 있으므로 JPA는 주문 컬렉션을 즉시 로딩하려고
다음 엔티티를 추가로 실행한다. 

```bash
<입력>
JPQL : select * from member

SQL : select * from orders where member_ID=?

<결과>
select * from member
select * from orders where member_ID=1
select * from orders where member_ID=2
select * from orders where member_ID=3
select * from orders where member_ID=4
select * from orders where member_ID=5
select * from orders where member_ID=1
select * from orders where member_ID=2
select * from orders where member_ID=3
select * from orders where member_ID=4
select * from orders where member_ID=5
```
먼저 회원 조회로 5명의 엔티티를 조회하고 즉시조회에 따라 추기적으로 5번의 조회를 하게된다.
즉, 처음 실행한 SQL의 결과 수 만큼 추가로 SQL을 실행하는 것을 N+1문제라 한다.

### 지연 로딩
회원과 지연 로딩으로 설정하게 되면 **N+1 Error**가 발생하지 않는다.
```bash
JPQL : select * from member
```
를 입력하게 되면 **회원**엔티티만 조회한다. 이후 추가적으로 

```java
firstMember = members.get(0);
firstMember.getOrder().size(); //지연로딩 초기화
```

이 과정에서 다음과 같은 SQL은 다음과 같이 실행되며 지연로딩 초기화를 하게되면 결과적으로 위와 같은 문제가 발생하게 된다.
```bash
SQL : select * from orders where member_ID=?

for(Member member : members){
System.out.println("member = " + member.getOrders().size());
}

<결과>
select * from member
select * from orders where member_ID=1
select * from orders where member_ID=2
select * from orders where member_ID=3
select * from orders where member_ID=4
select * from orders where member_ID=5
select * from orders where member_ID=1
select * from orders where member_ID=2
select * from orders where member_ID=3
select * from orders where member_ID=4
select * from orders where member_ID=5
```

## JPQL 페치 조인
글로벌 페치 전략을 즉시로딩으로 설정하면 어플리케이션 전체에 영향을 주어 비효율적이 된다. 때문에 JPQL을 호출하는 시점에 함께 로딩할 엔티티를 선택할 수 있는 페치 조인을 확인해야한다.
여기서 JPQL에 fetch join 을 넣어준다면 SQL join을 사용해서 페치 조인 대상까지 함께 조회한다.

```bash

< 패치 조인 사용 전 >

JPQL : select o from Order O

SQL : select * from Order

< 패치 조인 사용 후 >

JPQL : select o 
        from Order O
            join fetch 0.member
            
SQL : select o.* , m.* 
        from Order o
            join Member m on o.MEMBER_ID = m.MEMBER_ID
```
#### 문제 및 해결
무분별 사용시 사용화면에 맞춘 레포지토리 메소드가 증가할 수 있다. 결국 프레젠테리션 계층이 알게 모르게 데이터 접근 계층을 침범하는 것이다.
각 화면(A, B)에 필요한 데이터를 레포지토리부터 따로 가져올 필요없이 fetch join으로 두 엔티티를 함께 조회하는 방식을 사용하는 것이 로딩시간이 늘어나지만 
반대로 성능이 개선되는 장점이 있다. 

```bash
<페치조인 적용 전>

각 엔티티가 가지고있는 데이터에 침법할 수 있음

A entity 조회 : repository.findOne();

B entity 조회 : repository.findOneWithName();


<페치조인 적용 후>

A entity 조회 : 
@Query("select a from Academy a join fetch a.subjects s join fetch s.teacher")
repository.findOne();
```

### 강제 초기화
강제 초기화는 영속성 컨텍스트가 살아있을 대 프레젠테이션 계층이 필요한 엔티티를 강제로 초기화해서 반환하는 방법이다.

```java
class OrderService {
    @Transactional
    public Order findOrder(id){
        Order order = orderRepository.findOrder(id);
        order.getMember().getName();  // 프록시 객체를 강제로 초기화 한다.
        return order;
    }
}
```

글로벌 페치 전략을 지연 로딩으로 설정하면 연관된 엔티티를 실제 엔티티가 아닌 <u>프록시 객체</u>로 조회한다. 여기서 프록시 객체는 실제 사용하는 시점에서 
초기화 된다. 
또한 하이버네이트를 사용하면 initialize() 메소드를 사용해서 프록시를 강제로 초기화 할수 있다.
```
org.hibernate.Hibernate.initialize(order.getName());
```

프록시를 초기화 하는 역할을 서비스 계층이 담당하면 뷰가 필요한 엔티티에 따라 서비스 계층의 로직을 변경해야하는데 계층 침범 상황이 발생할 수 있다.
때문에 서비스 계층에서 프레젠테이션 계층을 위한 프록시 초기화 역할을 분리해야하는데 FACADE 계층이 역할을 담당한다.


### 정리
N+1문제에 대해서는 JPA에서는 지연로딩을 사용하는 것을 권장한다. N+1문제 뿐만 아니라 불필요한 엔티티를 로딩할 필요가 없어지기 때문인다. 
그리고 즉시로딩의 문제점은 반복적인 즉시 로딩이 실행될 경우 <u>예상하지 못한 SQL이 실행될 가능성</u>과 동시에 <u>성능 최적화의 어려움</u>이다.
그럼에도 즉시로딩이 필요한 경우에는 <u>JPQL페치 조인</u>을 사용하는 것을 권장한다.

> @OnetoOne, @ManytoOne : FetchType.EAGER (default)
> 
> @OnetoMany, @ManytoMany : FetchType.LAZY (default)

기본값이 즉시 로딩인 @OnetoOne, @ManytoOne은 **fetch=FetchType.LAZY**로 설정해서 지연로딩 전략을 사용하도록 권장한다.


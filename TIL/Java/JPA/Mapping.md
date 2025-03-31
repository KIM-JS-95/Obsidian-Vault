# 목차
> 1. 방향
> 	1. 단방향
> 	2. 양방향
> 2. 매핑
> 	1. [[#연관관계 주인(mappedBy)]]
> 	2. [[#mappedBy 설정시 이점]]
> 	3. [[#주인의 역할]]
> 	4. [[#JPA에서의 객체 관계 매핑]]
> 	5. [[#연관관계 편의 메서드]]

## 1. 방향
### 단방향
1. 객체 간의 관계를 한 방향으로만 매핑한다.
	- 한쪽 방향으로의 접근이 가능한 매핑으로 `Contents -> User` 혹은 `User -> Contents` 방식
### 양방향
2. 객체간의 관계를 양쪽으로 매핑한다.
  - 양방향 으로의 접근이 가능한 매핑으로 `회원 <--> 팀` 서로의 객체를 참조하는 방식이다.
  - 한 객체가 다른 객체를 참조하고 역방향으로 다시 참조가 가능한 매핑 방식

> 이러한 관계는 **객체 관계에서만 가능하고 테이블 관계는 항상 양방향 상태이다.**

![[매핑예제.canvas]]
## 2. 매핑

### 테이블과 객체의 연관관계 차이

**객체에는 양방향 연관관계의 개념은 존재하지 않으며** 단지, 서로 다른 단방향 연관관계의 2개의 객체를 로직으로 묶어서 양방향 처럼 보이게 할 뿐이다.

[[JPA]]는 이러한 [[ORM#패러다임|ORM패러다임]]을 해결하기 위해 두 객체의 연관관계 중 한쪽을 정하여 테이블의 외래 키를 관리하는 방식을 제공한다. 

### 연관관계 주인(mappedBy)

양방향 관계에서는 외래 키를 관리할 객체를 명시해야 한다.
이를 통해 **양방향 관계의 일관성과 유지보수가 용이해지며** 주로 '주체'가 될 부모 객체와 자식 객체가 관계를 명시하기 위해 사용되는 값은 `유일성`이 보장되는 필드가 사용 되어야하며 개발자는 [[#^36004e|@JoinColumne]] 을 사용하여 명시할 수 있다.
### mappedBy 설정시 이점
1. **일관성 있는 관계 설정**: 양방향 관계에서 주인 엔티티의 필드를 기반으로 관계가 설정되므로, 관계 설정이 일관적이며 안정적임 
2. **데이터 정합성 보장**: 양방향 관계의 한쪽 엔티티만을 수정해도 관계가 정확하게 유지되므로 데이터 정합성이 보장
4. **단순화된 코드**: 주인 엔티티에서만 매핑 정보를 관리하므로 코드가 단순함 
5. **성능 향상**: 양방향 관계를 설정시 쓸데없는 업데이트 쿼리를 방지하여 성능 저하를 방지할 수 있다.

### 주인의 역할
연관관계의 주인만이 DB 연관관계와 매칭되고 외래 키를 관리 할 수 있다.

- 주인은 `mappedBy` 속성을 사용하지 않는다.
- 주인이 아니면 `mappedBy` 속성을 사용하여 연관관계 주인을 지정해야한다.

### JPA에서의 객체 관계 매핑

[[JPA]]에서 제공하는 `@JoinColumn`은 대상 객체의 속성을 자신의 외래 키로 사용하도록 해준다.
`@OneToMany` 혹은 `@ManyToOne` 관계에서 모두 사용 가능하지만 일반적으로 다수의 엔티티 쪽에서 단일 엔티티를 참조하므로 `@ManyToOne`에서 사용한다. ^36004e
```java
@Entity
public class Parent {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
        
    @OneToMany(mappedBy='Parent')
    private List<Child> children;
}

@Entity
public class Child {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
        
    @ManyToOne
    @JoinColumn(name = "parent_id", nullable = false)
    private Parent parent;
}
```
### 연관관계 편의 메소드
양방향 연관관계에서 결국 양쪽을 모두 신경써야 한다면 하나의 코드처럼 사용하는 것이 좋다.

그러나 `팀 - 멤버` 관계에서 외래키를 가지는 멤버 엔티티의 외래키가 바뀔경우 기존의 외래키를 삭제하고 
새로운 키를 입력해 주어야한다. 

```java
public class Content{
    private User user;
    
    public void setUser(User user){ // 호출된 객체의 기존 데이터 유뮤 확인
        if(this.user != null){
            this.user.getContents().remove(this); // setUser 호출시 관계 갱신
        }
        this.user=user;
        user.getContents().add(this);
    }
}
```

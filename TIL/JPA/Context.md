# 영속성 컨텍스트

JPA 프로세스의 근본이자 가장 중요한 요소가 `컨텍스트`이다.

이 영속성 컨텍스트는 JPA 작업중에 개발자가 `commit` 혹은 `flush` 하기 전까지 DB에 저장하지 않고
SQL 쿼리문을 계속에서 `컨텍스트`에 저장 하도록 되어있다.

## 영속성 컨텍스트의 구성

### 1차 캐시


영속성 컨텍스트에는 작업 대상이 될 엔티티를 `1차 캐시`에 저장하도록 되어있다.

![](https://velog.velcdn.com/images%2Fxohoonx2%2Fpost%2Fdccee6e4-28a3-4e4f-a919-06d7c6586c17%2Fimg%20(1).png)

그리고 엔티티 조회시 DB를 거치치 않고 1차 캐시를 우선적으로 조회하도록 하며 데이터가 없을경우 DB에서 조회 후 엔티티를 `1차 캐시`에 저장한 후에 
영속 생태를 반환한다.

![](https://velog.velcdn.com/images%2Fxohoonx2%2Fpost%2F668feffb-dd5a-433d-a36d-edf24c07849b%2Fimg.png)

### 쓰기 지연 SQL 저장소

엔티티 `insert`, `delete`, `update` 작업시 쿼리를 1차 캐시 혹은 DB에 매번 작업처리하는 것이 아닌 `쓰기 지연 SQL 저장소`에 저장 후 
`flush` 후 한번에 작업을 수행하게 된다.

![](https://velog.velcdn.com/post-images%2Fconatuseus%2F51c8cae0-d09c-11e9-b275-49c1db32880d%2Fimage.png)

## update vs insert , delete

컨텍스트를 구성하는 것은 `1차 캐시`와 `쓰기 지연 SQL 저장소`이며 insert , delete의 경우 모든 쿼리작업을 SQL 저장소에 저장 후 
`commit` 작업을 통해 일괄적으로 작업이 이루어진다.

![](https://velog.velcdn.com/post-images%2Fconatuseus%2Feb6c9c30-d09c-11e9-b0db-1597a34a142f%2Fimage.png)

### update 또한 일괄적으로 작업을 해야할까?

개발자가 엔티티를 업데이트 한다면 **동일한 데이터를 바탕으로 작업이 이어서 이루어져야 할 것이다.**

즉, update 또한 `cummit`후 SQL 작업이 이루어진다면 엔티티는 개발자의 의도대로 흘러가지 않을 것이다.

JPA는 updata 작업의 `동일성 위배`를 해결하기 위해 updata 쿼리가 감지된다면 즉시 `flush` 가 작동하도록 개발하였다.

`컨텍스트`는 엔티티를 `1차 캐시`에 저장하는 과정에서 최초 엔티티와 수정 엔티티의 변경 요소를 확인할 수 있도록 `스냅샷`을 저장하고
지속적으로 변경 요소를 찾는다.

**이러한 기능을 `변경감지(dirty checking)`한다.**

대상 엔티티가 영속 상태에 있다면 `변경감지(dirty checking)` 기능이 지속적으로 작동하여 
개발자가 별도로 엔티티를 `save` 하지 않아도 자동적으로 `flush`를 수행한다. 

![](https://velog.velcdn.com/post-images%2Fconatuseus%2Fb5d57200-d0a0-11e9-90a8-3bdc8e61daef%2Fimage.png)

## JPA가 영속성 컨텍스트를 고집하는 이유

컨텍스트와 DB 데이터의 엔티티의 `동일성을 유지` 그리고 `반복적인 DB 접근으로 인한 성능 저하`를 제거하기 위해 
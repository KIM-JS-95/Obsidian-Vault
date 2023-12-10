# Common Table Expression

`WITH` 절과 함께 사용되는 `CTE`는 Mysql 8.0 부터 사용할 수 있다.

CTE는 기존의 뷰, 파생 테이블, 임시 테이블 등으로 사용되었던 것을 대신할 수 있으며, 더욱 간결한 식으로 표현할 수 있도록 구성할 수 있다.

어쩌면 SubQuery를 대신할 수 있다고 생각한다.

## CTE 구성

CTE는 가상의 테이블을 하나 더 생성한다 라고 생각하면 이해할 수 있다.

```mysql-sql
WITH CTE_TableName(열 이름)
AS
(
<쿼리문>
)
```

위 명령어로 만들어낸 테이블을 쿼리문의 **대상 테이블 이름**으로 사용할 수 있다.

### 지역별로 성적을 구하는 테이블

```mysql-sql

WITH CTE_TableName(addr, student)
AS
(
select * from grade_Table group by addr;
)

select addr, avg(student) from CTE_TableName group by addr;
```
## CTE , 뷰 차이점
CTE는 뷰와 그 용도는 비슷하지만 CTE는 1회성 쿼리문의 성질을 가지고 있다.

때문에 이미 사용한 CTE 테이블은 자동으로 삭제되어 다음 쿼리문에서는 사용할 수 없는 테이블이 되어진다.

## 정리
이전 복잡한 쿼리를 작성해야하는 경우 Sub쿼리문 혹은 임시 테이블을 만들어 가며
단계별로 테이블을 정리해 가며 올라갔던 방법과 비교한다면, 이전보다 더 쉽게 SQL문을 작설할 수 있을 것이다.



## Union vs Union All 차이

UNION: only keeps unique records

두 쿼리문의 결과에서 합집합을 구한다. (A∪B - A∩B)

UNION ALL: keeps all records, including duplicates

두 쿼리문의 결과에서 합집합을 구한다. 단, 중복되는 정보도 포함하여 출력한다. A∪B


## 처리 과정

1. 최종 UNION [ALL | DISTINCT] 결과에 적합한 임시 테이블(Temporary table)을 메모리 테이블로 생성
2. UNION 또는 UNION DISTINCT 의 경우, Temporary 테이블의 모든 컬럼으로 Unique Hash 인덱스 생성
3. 서브쿼리1 실행 후 결과를 Temporary 테이블에 복사
4. 서브쿼리2 실행 후 결과를 Temporary 테이블에 복사
5. 만약 3,4번 과정에서 Temporary 테이블이 특정 사이즈 이상으로 커지면 Temporary 테이블을 Disk Temporary 테이블로 변경  
              **(이때 Unique Hash 인덱스는 Unique B-Tree 인덱스로 변경됨)**
6. Temporary 테이블을 읽어서 Client에 결과 전송
7. Temporary 테이블 삭제

### 차이점 && 성능

각 `Union`의 차이는 중복제거를 위한 임시 테이블에 인덱스를 생성의 유무이다.

만일 처리중 데이터의 크기가 작아서 5번 과정을 거치지 않는다면 
메모리 Temporary 테이블에 `Hash 인덱스`를 사용하기 때문에 속도 차이가 발생한다.

그러나 테이블의 크기가 임시 테이블의 크기보다 커진다면 B-tree 인덱스 형태로 저장되기 때문에
처리 시간에 큰 차이가 발생하게된다.

즉, 쉽게 사용되는 `Union` 명령어는 **상대적으로 좋지 못한 성능**을 발생시키는 것이다.


### 중복을 처리하는 기준

완성된 두 테이블에서 중복을 제거하는 기준은 뭘까?

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile2.uf.tistory.com%2Fimage%2F999E59475C890DEB03CD6C)

결과를 출력해본다면 모든 컬럼들 사이에는 어떠한 중복도 없는 것을 볼 수 있다.

** 즉, 모든 컬럼이 중복체크 대상이 되는 것이다. **


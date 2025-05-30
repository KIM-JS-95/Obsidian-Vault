
# Cluster

DB를 통해 데이터를 조회할 경우 시간 효율을 높이기 위해 자주 사용되는 테이블 데이터를 
디스크의 같은 위치에 저장시키는 방법

인덱스에서 데이터를 조회하는 방법으로 구분할 수 있는 기술로 Non-Cluster / Cluster 로 구분되며 두 방식은 서로 다른 장점을
보여주기 때문에 상황에 맞춰 적용하면 될것이다.


## 특징
- 단위 테이블당 한 개의 클러스터를 생성하며 행 데이터를 물리적으로 열에 맞추어 자동 정렬한다. 

- 인덱스 자체의 리프 페이지가 곹 데이터 페이지 이므로 인덱스 자체에 데이터가 포함되어 있다 말할 수 있다.

- NonCluster 와 반대로 검색(Search) 속도가 매우 빠르다. 
- 어느 테이블이던지 한개의 클러스터를 생성할 수 있지만 **어느 열의 인덱스에 생성하냐에 따라 성능이 달라진다.**

## 장점

- 클러스터형 인덱스는 최대, 최소, 개수 유형 쿼리를 사용하여 범위 또는 그룹화에 이상적인 옵션
- 이 유형의 인덱스에서 검색은 데이터의 특정 지점으로 바로 이동할 수 있으므로 거기에서 순차적으로 읽을 수 있다.
- 클러스터형 인덱스 방법은 위치 메커니즘을 사용하여 범위 시작 부분에서 인덱스 항목을 찾는다.
- 검색 키 값의 범위를 요청할 때 범위 검색에 효과적인 방법
- 페이지 전송을 최소화하고 캐시 적중을 최대화하는 데 도움이 된다.

## 단점

- 비순차적으로 많은 인서트
- 클러스터형 인덱스는 데이터 페이지와 인덱스 페이지를 포함하는 많은 상수 페이지 분할을 생성
- 삽입, 업데이트 및 삭제를 위한 SQL에 대한 추가 작업
- 클러스터형 인덱스는 클러스터형 인덱스의 필드가 변경될 때 레코드를 업데이트하는 데 더 오랜 시간 소요
- 리프 노드는 대부분 클러스터형 인덱스의 데이터 페이지를 포함
- 
# Non - Cluster

## 특징
- 인덱스를 생설할 때는 데이터 페이지는 그냥 둔 상태에서 별도의 페이지에 인덱스를 구성한다.
- NonCluster 인덱스 자체의 리프 페이지는 데이터가 아닌, RIP `데이터가 위치하는 포인터`이다.
- NonCluster는 여러개의 인덱스를 생성할 수 있지만 **과도한 생성은 시스템 성능 저하**를 보여준다.

## 장점

- 비클러스터링 인덱스를 사용하면 데이터베이스 테이블에서 데이터를 빠르게 검색할 수 있다.
- 클러스터형 인덱스와 관련된 오버헤드 비용을 방지하는 데 도움
- 테이블에는 RDBMS에서 클러스터되지 않은 인덱스가 여러 개 있을 수 있습니다. 따라서 둘 이상의 인덱스를 만드는 데 사용할 수 있다.

## 단점

- 클러스터되지 않은 인덱스를 사용하면 데이터를 논리적 순서로 저장할 수 있지만 데이터 행을 물리적으로 정렬할 수는 없다.
- 클러스터되지 않은 인덱스에 대한 조회 프로세스는 비용이 많이 든다.
- 클러스터링 키가 업데이트될 때마다 클러스터링 키를 저장하는 클러스터되지 않은 인덱스에 해당 업데이트가 필요

## Cluster vs Non-Cluster

|😀|Cluster|Non-Cluster|
|:---:|:---:|:---:|
|속도|검색 우수| 입력 / 수정 / 삭제 우수|
|용량| 작은 용량 | 큰 용량 (별도의 인데스 페이지 생성)|
|정렬| 자동 재배열| X |
|선택도|30 % 이내에서 사용요 구| 3% 이내에서 사용 요구|
|최대 갯수| 1개 / 테이블| 249개 / 테이블|

## 🧾Reference

[Clustered vs Non-clustered Index: Key Differences with Example](https://www.guru99.com/clustered-vs-non-clustered-index.html)
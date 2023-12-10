# Spanning Tree

그래프 내의 모든 정점을 포함하는 트리를 의미
> n개의 정점을 가지는 그래프의 간선의 수 (n-1)로 이루어져 있다.

DFS, BFS을 이용하여 그래프에서 신장 트리를 찾을 수 있으며 하나의 그래프에는 많은 신장 트리가 존재할 수 있다.
Spanning Tree는 트리의 특수한 형태이므로 모든 정점들이 연결 되어 있어야 하고 *사이클*을 포함해서는 안된다.
따라서 <u>Spanning Tree는 그래프에 있는 n개의 정점을 정확히 (n-1)개의 간선으로 연결 한다.</u>

### 최소 신장트리 (MST)
Spanning Tree 내에서 노드간의 간선의 합이 값이 최소인 트리를 의미한다.

MST Algorithm 을 구현하는 방법은 4가지가 존재한다.

1. 크루스칼 알고리즘
2. 위상 정렬 알고리즘
3. 다익스트라 알고리즘
4. 플로이드 워셜 알고리즘

---

### 그래프 알고리즘

#### 간선 선택을 기반으로 하는 알고리즘

1. Kruskal Algorithm

Greedy를 이용하여 모든 정점을 최소비용으로 하여 답을 구하는 방법이며 최초 간선들의 가중치를 
**오름차순** 으로 정렬한 상태에서 진행한다.

2.  Floyd Algorithm

거쳐가는 노드 기준으로 최단 거리를 갱신하는 방법으로 모든 지점에서 모든 지점까지의 최단 경로를 구할 경우 적용한다.
![1](https://t1.daumcdn.net/cfile/tistory/99D9634B5C31877A26)
> DB(a,b) = min(DB(a,b), DB(a,c)+DB(c,b))

---

#### 정점 선택기반의 알고리즘

3. Topological Sort

그래르의 모든 노드들이 방향성에 거스르지 않도록 수서대로 나열하는 정렬 기법으로 주로 '학습 순서 설정 문제' 등에서 적용한다.
즉, 방향 그래프에 존재하는 각 정점들의 선행 순서를 위배 하지 않으면서 모든 정점을 나열하는 알고리즘

4. Dijkstra Algorithm
단계마다 방문하지 않는 노드 중에서 가장 <u>최단거리가 짧은 노드를 선택</u>한 뒤에 노드를
   거쳐 가는 경우를 확인하여 최단거리를 갱신하는 방법으로 한 지점에서 다른 지점가지의 최단 경로를 확인할때 사용한다.
   

### 그래프 vs 트리

|*|그래프|트리|
|:---:|:---:|:---:|
|방향성|방향/무방향| 방향|
|순환성|순환/비순환|비순환|
|루트 노드 존재 여부|없음|있음|
|노드(부모/자식) 관계성|무관계|관계|
|모델|네트워크 모델|계층 모델|


### 🧾Reference
1. [compare Graph Algorithms](https://data-make.tistory.com/527)
2. [Spanning Tree](https://gmlwjd9405.github.io/2018/08/28/algorithm-mst.html)

<a link=“https://programmers.co.kr” https://programmers.co.kr> </a>

<a href=“https://programmers.co.kr”> https://programmers.co.kr </a>

 
 
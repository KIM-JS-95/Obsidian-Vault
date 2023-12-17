# 🐋 Docker Logging 🐋

시스템이 정상적으로 운영됨을 확인하고 발생된 문제에 대한 디버깅을 효율적으로 관리하고자 한다면, 컨테이너 모니터링은 필수 이다.

## 🦐 도커 기본 로깅

도커가 제공하는 기능으로 별도의 인자를 명시하지 ㅇ낳았거나 다른 로딩 SW를 설치하지 않았다면, `**.log`파일로 남긴다.

```shell
docker logs <Container Name>
```

### 기본 로깅 단점
- STDOUT / STDERR 만 처리하므로 로그를 파일로만 기록할 수 있다.
- 컨테이너가 운영중에 있다면 기본 로깅 기능은 log를 계속해서 기록하여 사용자의 디스크 용량을 잡아먹을 것이다.

## 🦐 ELK 를 이용한 로깅

![제목 없음](https://user-images.githubusercontent.com/65659478/171559548-2abf6a69-08da-45b4-bb8c-8cee3d1e942c.png)

### Elasticsearch

준 실시간 검색 기능을 제공하는 텍스트 검색 엔진이다. 

대용량의 데이터 처리를 위해서 여러 개의 노드로 쉽게 확장이 가능하도록 설계되었고, 대량의 로그 검색에 적합하다.

### Logstash

원시 로그를 읽기 위한 도구로, 로그를 분석하고 필터링하여 인덱스 또는 저장소와 같은 다른 서비스로 로그를 전달한다.

### Kibana

일레스틱서치에 대한 JS 기반의 그래픽 인터페이스이다. 

일레스틱서치 쿼리를 실행하고 결과를 다양한 차트로 시각화할 때 사용된다.


## 🦐 ELk + Logspout 설계

![](https://miro.medium.com/max/1400/0*qxW9DS-RGveqqwBQ.png)

그러나 `LOG 수집기`에는 여러 방식이 있지만 Docker API 친화적인 `logspout` 를 사용할 것이다.

자세한 파일 구성은 [Repository](https://github.com/KIM-JS-95/PillI-Info-Service) 를 참고해 주세요.

### DIR Tree

```
PILLSSERVICE_BE
│
├─ ...
│
├─ elk
│  ├─ elasticsearch
│  │  └─ config
│  ├─ kibana
│  │  └─ config
│  └─ logstash
│      └─ config
├─ gradle
│  └─ wrapper
├─ presentation
├─ proxy
│  └─ conf
└─ src
    └─ main
        ├─ java
        │  └─ ...
        │
        └─ resources
            ├─ ...
```


### docker-compose

```shell
version: '3.0'
services:

  ...

-----  1

  logspout:
    container_name: logspout
    image: gliderlabs/logspout:latest
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    links:
      - logstash
    ports:
      - "8000:80"
    command: syslog+tls://logstash:5000
    depends_on:
      - logstash
      - kibana
      - elasticsearch
    networks:
      - elk
    restart: always

-----  2

  logstash:
    build: elk/logstash/
    container_name: logstash
    volumes:
      - ./elk/logstash/config:/etc/logstash/conf.d
    links:
      - elasticsearch
    environment:
      LOGSOUT: ignore
    command: -f /etc/logstash/conf.d/
    ports:
      - "5000:5000"
    networks:
      - elk

-----  3

  kibana:
    build: elk/kibana/
    container_name: kibana
    volumes:
      - ./elk/kibana/config/:/opt/kibana/config/
    ports:
      - "5601:5601"
    links:
      - elasticsearch
    environment:
      LOGSOUT: ignore
      ELASTICSEARCH_URL: http://elasticsearch:9200
    networks:
      - elk
    depends_on:
      - elasticsearch

-----  4

  elasticsearch:
    build: elk/elasticsearch/
    volumes:
      - ./elk/elasticsearch/config/:/opt/elasticsearch/config/
    container_name: elasticsearch
    ports:
      - "9200:9200"
      - "9300:9300"
    environment:
      ES_JAVA_OPTS: "-Xms2g -Xmx2g"
      discovery.type: single-node
    networks:
      - elk

networks:
  elk:
    driver: bridge
```

### 1. logspout

`Logspout` 은 Docker 컨테이너 로그용으로 특별히 설계된 오픈 소스 로그 라우터이며
동일한 호스트에서 실행되는 다른 모든 컨테이너에서 로그를 수집한 다음 선택한 대상으로 전달하는 역할을 수행한다.


해당 이미지 사용은 Docker Hub Repo를 확인해야한다. 

`commend: ~~` 의 경우 블로그에 따라 다르기 때문에 **문서를 따라 설정하는 것이 좋은 방법이다.**

### 2. logstash

로그 및 데이터 수집 및 변환 에이전트 역할을 수행하다.

`configuration`에서 설정된 포트와 파일 형식에 따라 `Logstash`는 ElasticSearch으로 정보를 전송하게 된다.

### 3. kibana

Elasticsearch의 빠른 검색을 통해 데이터를 시각화 및 실시간 모니터링을 수행하는 Tool 이다.


### 4. Elasticsearch

Elasticsearch는 Apache Lucene에 구축되어 배포된 실시간 검색 및 분석 엔진으로

`logstash`로 부터 받은 데이터를 DataMining 하여  로그 분석, 전체 텍스트 검색, 보안 인텔리전스, 비즈니스 분석 및 운영 인텔리전스 사용 사례에 일반적으로 사용된다.

Window 에서 다음 에러가 발생하는 경우 다음과 같이 조치해 주세요


    ERROR: [1] bootstrap checks failed es01 | [1]: max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]


```shell
## Docker 시스템 접속
wsl -d docker-desktop

## 도커 자체 최대 용량 변경
sysctl -w vm.max_map_count=262144

```

multi node 에러의 경우 `ver.7.xx` 이후부터 발생하지 않는다 발표했지만 

발생하는 경우 `environment`에 다음과 같이 추가하자

```shell
discovery.type: single-node
```


 


## Result
![제목 없음](https://user-images.githubusercontent.com/65659478/171555730-fe27fc17-968e-4688-b9e5-4454d0851935.png)

## Repository

- [PillService_Repo](https://github.com/KIM-JS-95/PillI-Info-Service)

# 🐋 Reference
- [제대로 배우는 도커](http://www.yes24.com/Product/Goods/34648781)
- [elastic](https://www.elastic.co/kr/what-is/elk-stack)
- [docker-compose ERROR: bootstrap checks failed - StackOverFlow](https://stackoverflow.com/questions/57998092/docker-compose-error-bootstrap-checks-failed-max-virtual-memory-areas-vm-ma)
# 🐋 Docker network 🐋


Docker 컨테이너(container)는 격리된 환경에서 돌아가기 때문에 기본적으로 다른 컨테이너와의 통신이 불가능하다. 
하지만 여러 개의 컨테이너를 하나의 Docker 네트워크(network)에 연결시키면 서로 통신이 가능하다.

![img.png](../images/img.png)

## 🦐 Driver (네트워크 종류)

- bridge
  - 기본 네트워크 드라이버이다. `브리지 네트워크`는 일반적으로 애플리케이션이 통신이 필요한 독립 실행형 컨테이너에서 실행될 때 사용한다.

- host
  - 독립형 컨테이너의 경우 컨테이너와 Docker 호스트 간의 네트워크 격리를 제거하고 호스트의 네트워킹을 직접 사용한다.

- overlay
  - 오버레이 네트워크는 여러 Docker 데몬을 함께 연결하고 스웜 서비스가 서로 통신할 수 있도록 한다. 
  - 오버레이 네트워크를 사용하여 Swarm 서비스와 독립 실행형 컨테이너 간 또는 서로 다른 Docker 데몬에 있는 두 개의 독립 실행형 컨테이너 간의 통신을 용이하게 할 수 있다.
  - 이 전략을 사용하면 이러한 컨테이너 간에 OS 수준 라우팅을 수행할 필요가 없다.

- ipvlan
  - IPvlan 네트워크는 사용자에게 IPv4 및 IPv6 주소 지정에 대한 완전한 제어를 제공한다. 
  - VLAN 드라이버는 운영자가 언더레이 네트워크 통합에 관심이 있는 사용자를 위해 레이어 2 VLAN 태깅 및 IPvlan L3 라우팅을 완벽하게 제어할 수 있도록 하기 위해 그 위에 구축된다.

- macvlan
  - Macvlan 네트워크를 사용하면 컨테이너에 MAC 주소를 할당하여 네트워크에서 물리적 장치로 표시할 수 있다.
  - Docker 데몬은 MAC 주소로 컨테이너로 트래픽을 라우팅합니다. 
  - macvlan Docker 호스트의 네트워크 스택을 통해 라우팅되지 않고 물리적 네트워크에 직접 연결될 것으로 예상되는 레거시 애플리케이션을 처리할 때 드라이버를 사용하는 것이 때때로 최선의 선택이다.

- none
  - 이 컨테이너의 경우 모든 네트워킹을 비활성화한다. 
  - 일반적으로 사용자 지정 네트워크 드라이버와 함께 사용됩니다. 
  - none스웜 서비스에는 사용할 수 없다.


## 🦐 network 명령어
### 생성
  - docker network create <Option> [네트워크]
  
### 상세 정보
  - docker network inspect <Option> [네트워크 이름]
### 연결
  - docker network connect <Option> [네트워크] [컨테이너]
### 연결 해제
  - docker network disconnect <Option> [드라이버] [컨테이너]
### 삭제
  - docker network rm <Option> [네크워크 이름]
### 청소
  - docker network prune

## 🦐 컨테이너 간 네트워킹

### 테스트
    docker exec [컨테이너 1 혹은 IP] ping [컨테이너 2 혹은 IP]


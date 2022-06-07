# Docker in Docker

Jenkins CI 를 구성하는 중 Docker-compose를 실행하기 위해서는 Jenkins container 내부에 Docker를 다시한번 설치해야 한다는 것을 알았다.



도커가 컨테이너를 구성하기 위해서는 크게 2가지가 있음을 알았고 이를 정리한다.

## DinD

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FXLxyZ%2FbtroVr1OTaR%2F27VHLse6YwjcoEZ4vFqqj1%2Fimg.png)

도커 컨테이너 내부에서 도커를 실행하는 방식이다.

- 저체적인 캐시를 사용하게 되기 때문에 처음에는 빌드가 느리고 자신의 이미지 전체를 다시 끌어와야한다.
- 컨테이너가 특별한 권한을 가진 모드(`--privilige`)에서 실행되어야 하기 때문에 `DooD` 방법보다 안전하지 않다.
- DinD는 `/var/lib/docker` 디렉토리를 위해 볼륨을 사용하는데 컨테이너를 제거할 경우 같이 제거하지 않으면 빠르게 사용 가능한 디스크 공간이 줄어들 수 있다.

### [Jenkins + DInD - Docker Hub](https://hub.docker.com/r/jpetazzo/dind)

## DooD

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FkG4Ee%2Fbtro6axPOc6%2FuO8iaewJXKDifLnx0y1Oxk%2Fimg.png)

호스트 Docker 계층에서 실행하는 방식으로 `docker.sock`을 통해 데이터가 호스트 Docker로 전달된어  형제(sibling) 컨테이너로 구성되어진다.


- **호스트 OS와 이미지 공유 가능**
- 이미지를 여러 번 저장하지 않아도 됩니다.
- Jenkins가 로컬 이미지 생성을 자동화할 수 있도록 합니다.
- 감독자의 필요성 제거(여러 프로세스를 의미함)
- 가상화 계층(lxc) 제거
- 런타임에 더 큰 유연성을 허용합니다.
- **젠킨스(sudo) 사용자가 접두사 docker없이 실행되도록 허용한다.**

### [Jenkins + DooD - Docker Hub](https://hub.docker.com/r/psharkey/jenkins-dood)


## DinD vs DooD

그림에서 알 수 있듯이 사용자가 Container를 어디로 올리는 지에 따라 방향성이 다르다.

`Jenkins`의 `Execute Shell`로 Docker를 실행한다면 Jenkins Container 내부에 실행되고 있는 것이다.

`DinD`를 사용하는 주된 장점은 **애플리케이션 실행을 위한 격리된 환경을 제공**한다는 점 이지만 단점으로 `보안성`과 `디스크 용량`의 문제를 가지고 있어
사용자가 신경써야할 부분이 많다.


## Error Log

1. Docker 실행 및 연결 문제
```shell
cannot connect to the docker daemon at unix:///var/run/docker.sock. is the docker daemon running?
  해결 -> sudo /etc/init.d/docker start
```

```shell
system has not been booted with systemd as init system (pid 1). can't operate.
  해결 -> sudo /etc/init.d/docker start
```

2. jenkins - Docker 권한 문제

```shell
#  cd /etc/sudoers

## Allow root to run any commands anywhere
root    ALL=(ALL)       ALL
# 추가
jenkins ALL=(ALL)       NOPASSWD: ALL

```



# Reference
- [Cannot connect to the Docker daemon at unix:/var/run/docker.sock. Is the docker daemon running? - StackOverFlow](https://stackoverflow.com/questions/44678725/cannot-connect-to-the-docker-daemon-at-unix-var-run-docker-sock-is-the-docker)
- [Execute Shell 명령어에서 sudo를 사용하기 위한 설정](https://velog.io/@livenow/Jenkins-Execute-Shell-%EB%AA%85%EB%A0%B9%EC%96%B4%EC%97%90%EC%84%9C-sudo%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-%EC%9C%84%ED%95%9C-%EC%84%A4%EC%A0%95)
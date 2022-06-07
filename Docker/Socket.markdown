# Docker Socket ??


![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FkG4Ee%2Fbtro6axPOc6%2FuO8iaewJXKDifLnx0y1Oxk%2Fimg.png)


도커 소켓은 클라이언트 데몬 간의 통신을 위한 엔드포인트를 말한다.

기본적으로 `/var/run/docker.sock` 파일을 통해 접근되는 IPC 소켓이지만, 도커는 네크워크 주소와 systemd 방식의 소켓으로 사용되는 TCP 소켓도 지원한다.

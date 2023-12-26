# API 방식과 Connect 방식

PHP FTP 방식에서 AWS S3로 마이그레이션 작업을 하는 일을 담당하게 되었다.

> 기존 FTP 메소드에서 S3로 변경했을때 바로 적용할 수 있도록 해주세요.

중요한것은 메소드의 매게변수와 그 기능들이 정상 작동할 수 있도록 구조를 변경하는 일이였다.

모든 언어가 가지고 있듯 FTP 의 경우 Connector 방식을 가지고 있어 `연결 -> 유지 -> 해제`의 Cycle을 가진다.

그렇다면 S3 API에도 Connection 상태를 컨트롤 할 수 있을까?


S3 `put_object()` API Documment를 살펴보면 연결상태 변경에 대한 정보는 찾을 수 없다.

`StackOverFlow`에서는 Connection 방식과 API 에서의 차이점을 이곳에 두고있다.

## Connector
`Connector`은 VPN 네트워크를 통한 통신 중심으로 인스턴스화를 시키거나 컨테이너로 사용할 수 있다.

![](https://blog.axway.com/wp-content/uploads/2020/04/api-and-connectors-2.jpg)


## API
`Application Programming Interface`는 서보를 향하는 `End-Point`의 집합체로서 서비스 레이어에서 제공하는 인터페이스 개념이다.

즉, access point + End point 를 지정하여 명세서 규칙에 따라 데이터를 요청하는 방식인것이다.

![](https://blog.axway.com/wp-content/uploads/2020/04/api-and-connectors-1.jpg)


## 정리
기존 Connector 방식에서 API 방식으로 변경하는 과정에서 state 관리는 필요가 없다. 때문에 별도 지정 후 관리가 필요 없다.

# Reference
-[The difference between an API and a connector: When do I use one? ](https://blog.axway.com/learning-center/apis/api-management/api-and-a-connector)
-[Can I use a funtion AWS `put_object()` API an option binary or ascii mode like a function PHP `ftp_put()`?](https://stackoverflow.com/questions/74189435/can-i-use-a-funtion-aws-put-object-api-an-option-binary-or-ascii-mode-like-a)

## 🚀 API(Application Programming Interface)

직역하자면 `응용 프로그래밍 명세서`이다.
목적은 프로그램들 혹은 컴퓨터와 컴퓨터 사이의 상호작용하는 것을 도와주는 매개체이다.


## 🚀 API는 어떻게 사용되어질까?

우리가 웹 개발을 진행하게되면 필요한 기능을 구현하게된다.
가장 기본적인 `CRUD` 또한 API로 볼수 있다.  

또한 `KAKAO`, `Google`, 심지어 `Discord` 까지 
최근 모든 서비스가 자신의 서비스를 응용할 수 있는 API를 지원하고 있다.

`Red Hat`은 API의 정의를 다음과 같이 하고있다.

>API는 애플리케이션 소프트웨어를 빌드하고 통합하기 위한 정의 및 프로토콜  세트
>
>API를 사용하면 구현 방식을 알지 못하는 제품 또는 서비스와도 통신할 수 있으며 애플리케이션 개발을 간소화하여 
시간과 비용을 절약할 수 있습니다. 
>
>새로운 툴과 제품을 설계하거나 기존 툴과 제품을 관리할 때 API를 사용하면 
<u>유연성을 높이고 설계, 관리, 사용 방법을 간소화하며 혁신의 기회를 얻을 수 있습니다.</u>

# API 방식과 Connect 방식

FTP 의 경우 Connector 방식을 가지고 있어 `연결 -> 유지 -> 해제`의 Cycle을 가진다.

그렇다면 S3 API에도 `Connection` 상태를 컨트롤 할 수 있을까?

AWS S3 API Documment `put_object()`를 살펴보면 연결상태에 대한 정보는 찾을 수 없다.

`StackOverFlow`에서는 Connection 방식과 API 에서의 차이점을 다음과 같이 보고있다.

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


### 🧾 Reference

[Red Hat API 개요](https://www.redhat.com/ko/topics/api/what-are-application-programming-interfaces)

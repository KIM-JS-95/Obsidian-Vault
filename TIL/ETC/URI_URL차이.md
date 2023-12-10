
# URI vs URL vs URN


![](https://www.charlezz.com/wordpress/wp-content/uploads/2021/02/www.charlezz.com-uri-url-uri-url-300x300.png)


## URI(Uniform Resource Identifier)

인터넷에 있는 자원을 나타내는 `식별자`이며 **인터넷에서 요구되는 기본조건으로서 인터넷 프로토콜에 항상 붙어 다닌다.** 

URI의 하위개념으로 URL, URN 이 있다

## URL(Uniform Resource Locator)

네트워크 상에서 리소스가 어디 있는지를 알려주기 위한 규약이다.

즉, 컴퓨터 네트워크와 검색 메커니즘에서의 위치를 지정하는, `웹 리소스`에 대한 참조이다. 

흔히 웹 사이트 주소로 알고 있지만, **URL은 웹 사이트 주소뿐만 아니라 컴퓨터 네트워크상의 자원을 모두 나타낼 수 있다.**

그 주소에 접속하려면 해당 URL에 맞는 `프로토콜(ex: http,  https)`을 알아야 하고, 그와 동일한 프로토콜로 접속해야 한다.


## URN(Uniform Resource Name)

URN은 영속적이고, 위치에 독립적인 자원을 위한 지시자로 사용하기 위해 1997년도 RFC 2141 문서에서 정의되었다.


## 어떻게 구문하는가?

예를 들어 `http://opentutorials.org:3000/main?id=HTML&page=12` 라고 되어있는 주소가 있다.

여기서 `http://opentutorials.org:3000/main` 까지는 URL이고(URI이기도 한)
`http://opentutorials.org:3000/main?id=HTML&page=12` 이 것은 URI라고 할 수 있다. (URL은 아님)


# Reference
- [Dev Scroll](https://inpa.tistory.com/entry/WEB-%F0%9F%8C%90-URL-URI-%EC%B0%A8%EC%9D%B4)
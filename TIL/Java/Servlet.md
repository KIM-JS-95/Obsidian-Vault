# 🚀 Servlet
클라이언트의 요청을 처리하고, 그 결과를 반환하는
Servlet 클래스의 구현 규칙을 지킨 `자바 웹 프로그래밍 기술`
다시말해, 자바 언어로 구현한 웹 어플리케이션이라는 말인데 이 때문에 `JSP`와 많이 비교된다.

## 🚀 Servlet Container (서블릿 컨테이너)

`Spring Boot` 개념이 등장하기 전 웹 어플리케이션으로 

![](https://gitlab.com/jongwons.choi/spring-boot-security-lecture/-/raw/master/images/fig-1-servlet-container.png)

- 톰켓과 같은 웹 애플리케이션을 서블릿 컨테이너라고 부르는데, 이런 웹 애플리케이션(J2EE Application)은 기본적으로 필터와 서블릿으로 구성되어 있습니다.
- 필터는 체인처럼 엮여있기 때문에 `필터 체인`이라고도 불리는데, 모든 request 는 이 필터 체인을 반드시 거쳐야만 서블릿 서비스에 도착하게 됩니다.


## 🌠 Servlet 특징

- 클라이언트의 요청에 대해 동적으로 작동하는 웹 어플리케이션 컴포넌트
- html을 사용하여 요청에 응답한다.
- Java Thread를 이용하여 동작한다.
- **MVC 패턴에서 Controller로 이용된다.**
- HTTP 프로토콜 서비스를 지원하는 javax.servlet.http.HttpServlet 클래스를 상속받는다.
- UDP보다 처리 속도가 느리다.
- HTML 변경 시 Servlet을 재컴파일해야 하는 단점이 있다.



# 🧾 Reference

- [Servlet JSP 차이](https://steady-coding.tistory.com/463)
- [기록공간](https://lipcoder.tistory.com/459)

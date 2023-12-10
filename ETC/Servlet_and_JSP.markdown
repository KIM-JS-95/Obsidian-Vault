---
layout: post
title:  "Servlet and JSP"
date:   2022-02-09 12:05:21 +0800
tags: Spring Web
color: rgb(154,133,255)
subtitle: Servlet JSP
--- 
### 🚀 JSP(JavaServer Pages)

JSP는 HTML내에 자바 코드를 삽입하여 웹 서버에서 동적으로 웹 페이지를 생성하여 웹 브라우저에 돌려주는 
서버 사이드 스크립트 언어이다. 
Java EE 스펙 중 일부로 웹 애플리케이션 서버에서 동작한다.

### 🚀 Servlet
클라이언트의 요청을 처리하고, 그 결과를 반환하는
Servlet 클래스의 구현 규칙을 지킨 `자바 웹 프로그래밍 기술`
다시말해, 자바 언어로 구현한 웹 어플리케이션이라는 말인데 이 때문에 `JSP`와 많이 비교한다.

### 🚀 Servlet Container (서블릿 컨테이너)

`Spring Boot` 개념이 등장하기 전 웹 어플리케이션으로 
![](https://gitlab.com/jongwons.choi/spring-boot-security-lecture/-/raw/master/images/fig-1-servlet-container.png)

- 톰켓과 같은 웹 애플리케이션을 서블릿 컨테이너라고 부르는데, 이런 웹 애플리케이션(J2EE Application)은 기본적으로 필터와 서블릿으로 구성되어 있습니다.
- 필터는 체인처럼 엮여있기 때문에 `필터 체인`이라고도 불리는데, 모든 request 는 이 필터 체인을 반드시 거쳐야만 서블릿 서비스에 도착하게 됩니다.



#### 🌠 서블릿 웹 페이지
```java
@WebServlet(name = "memberSaveServlet", urlPatterns = "/servlet/members/save")
public class MemberSaveServlet extends HttpServlet {

    private final MemberRepository memberRepository = MemberRepository.getInstance();

    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        final String username = request.getParameter("username");
        final int age = Integer.parseInt(request.getParameter("age"));
        final Member member = new Member(username, age);
        memberRepository.save(member);

        response.setContentType("text/html");
        response.setCharacterEncoding("utf-8");
        final PrintWriter printWriter = response.getWriter();
        printWriter.write("<html>\n" +
            "<head>\n" +
            " <meta charset=\"UTF-8\">\n" +
            "</head>\n" +
            "<body>\n" +
            "성공\n" +
            "<ul>\n" +
            " <li>id=" + member.getId() + "</li>\n" +
            " <li>username=" + member.getUsername() + "</li>\n" +
            " <li>age=" + member.getAge() + "</li>\n" +
            "</ul>\n" +
            "<a href=\"/index.html\">메인</a>\n" +
            "</body>\n" +
            "</html>");
    }
}
```

처음 SpringBoot로 개발을 시작한 나에게 있어서 Client 와 Server의 구분이 없어 가독성이 떨어지고
유지보수에서도 문제가 많아질 것을 느꼈다.

그래서 여기서 발전한 것이 `JSP`이다

#### 🌠 JSP 웹 페이지
```java
<%@ page import="hello.servlet.basic.domain.member.Member" %>
<%@ page import="hello.servlet.basic.domain.member.MemberRepository" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    final MemberRepository memberRepository = MemberRepository.getInstance();
    final String username = request.getParameter("username");
    final int age = Integer.parseInt(request.getParameter("age"));
    final Member member = new Member(username, age);
    memberRepository.save(member);
%>
<html>
<head>
    <title>Title</title>
</head>
<body>
성공
<ul>
    <li>id=<%=member.getId()%>
    </li>
    <li>username=<%=member.getUsername()%>
    </li>
    <li>age=<%=member.getAge()%>
    </li>
</ul>
<a href="/index.html">메인</a>
</body>
</html>
```

기존 서블릿이 JAVA에 HTML코드를 넣는 방식이라면 JSP는 그 반대의 방식을 적용한다.
그래도 아주 별로다 🤮🤮🤮🤮🤮

### 차이점
- Servlet
  - 자바코드로 구현하고 컴파일하고 배포해야 한다.
  - HTML태그로 문자열("")스크림으로 처리해야 한다.
  - 코드가 수정되면 다시 컴파일하고 배포해야 한다


- JSP
   - 키워드가 태그화 되어 서블릿에 비해 배우기 쉽다.
   - 자바코드를 <%%>태그 안에 처리해주어야 한다.
   - HTML처럼 태그를 사용하여 자바코드도 사용이 가능하다.


### 🌠 Servlet 특징

- 클라이언트의 요청에 대해 동적으로 작동하는 웹 어플리케이션 컴포넌트
- html을 사용하여 요청에 응답한다.
- Java Thread를 이용하여 동작한다.
- **MVC 패턴에서 Controller로 이용된다.**
- HTTP 프로토콜 서비스를 지원하는 javax.servlet.http.HttpServlet 클래스를 상속받는다.
- UDP보다 처리 속도가 느리다.
- HTML 변경 시 Servlet을 재컴파일해야 하는 단점이 있다.


### 🌠 JSP 특징

- 최초 서블릿으로 컴파일 된 후에는 메모리에서 처리되기 때문에 많은 사용자 접속도 원할히 처리된다.
- JSP 또한 다른 Servlet 간 데이터 공유가 용이하다.
- 자바를 기반으로 하고 있으므로 플랫폼에 독립적이다.
- (자바)빈즈라는 자바 컴포넌트를 사용할 수 있다.
- 대규모 어플리케이션을 구현할 때 사용되는 EJB(Enterprise Java Bean) 기술과 완벽하게 호환된다.
- 사용자 정의 태그를 만들어 사용할 수 있으며 JSTL과 같은 태그 라이브러리를 이용할 수 있다.
- HTTP와 같은 프로토콜에 따라 클라이언트의 요청을 처리하고 응답한다.
- HTML, XML 등 웹 서비스와 관련된 문서를 생성하는 데 주로 사용된다.
- JDBC(Java DataBase Connect) API를 사용하여 웹 어플리케이션에서 데이터베이스에 연결할 수 있다.
- 표현 언어, 표현식, 스크립트릿 등의 다양한 스크립트 요소와 액션 태그 등을 제공함으로써 더욱 쉬운        프로그래밍을 구현할 수 있다.
- 서블릿 컨테이너(ex. Tomcat)가 필요하다.



### 🧾 Reference

[Servlet JSP 차이](https://steady-coding.tistory.com/463)

[기록공간](https://lipcoder.tistory.com/459)

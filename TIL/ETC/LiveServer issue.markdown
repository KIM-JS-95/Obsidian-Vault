# Visual Studio

## VS Live Server Issue

Live Server 상에서 SpringBoot API 통신은 불가능 하다.

> net::err_aborted 405 (method not allowed)

이 말은 `Live Server`에서 AJAX 통신시 현재 페이지 에서는 해당 `Method`를 지원하지 않는다는 말이다.

`F12` 개발자 모드에서 Header 를 살펴본다면 지원하는 메소드를 볼 수 있는데 `Get`, `UPDATE`, `OPTION`이 있다.

`POST`가 빠져있는 것을 볼 수 있는데 `Live Server` 개발자 [ritwickdey](https://github.com/ritwickdey/vscode-live-server-plus-plus) 의 
말에 따르면 해당 `POST`에 대한 문제는 원인을 알 수 없다고 한다.

## 정리
Front-End 개발시 Live Server 사용은 **디자인 개발**에만 참고하자.

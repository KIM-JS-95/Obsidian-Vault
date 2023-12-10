---
layout: post 
title:  "SPRING JWT"
date:   2021-07-02 12:05:21 +0800 
tags: SpringBoot JWT
color: rgb(154,133,255)
subtitle: SPRING 보안 인증
--- 

## JSON Web Token?

JSON 웹 토큰(JSON Web Token, JWT, "jot”[1])은 선택적 서명 및 선택적 암호화를 사용하여 데이터를 만들기 위한 인터넷 표준으로, 
페이로드는 몇몇 클레임(claim) 표명(assert)을 처리하는 JSON을 보관하고 있다.

이를테면 서버는 "관리자로 로그인됨"이라는 클레임이 있는 토큰을 생성하여 이를 클라이언트에 제공할 수 있다. 그러면 클라이언트는 해당 토큰을 사용하여 관리자로 로그인됨을 증명한다.

## 구조
JWT는 크게 (Header , Payload , Sign) 3가지로 나뉘며 역할은 다음과 같다.

![JWT Structure](https://media.vlpt.us/images/ayoung0073/post/60e6ead1-620f-4e4f-8cad-f4e8110ee0a4/image.png)


| 구조 | 표현 | 역할 |
|:---:|---|---|
| Header | {<br>"alg" : "HS256",<br> "typ" : "JWT"<br>} | Token의 타입(jwt, jws 등)과 해시 암호화 알고리즘(HMAC/SHA256/RSA)으로 구성<br>Base64Url로 되어있지만 실제 데이터는 JSON 형태로 되어있음 |
| Payload |{<br>"loggedInAs" : "admin",<br>"iat" : 1422779638<br>} |토큰에 담을 claim 정보(사용자 정보)를 포함.<br> Payload에 담는 정보의 한 조각을 클레임이라 하고, key / value의 한 쌍으로 이루어져 있다.<br> 토큰에는 여러개의 클레임을 넣을 수 OHeader와 Payload는 Base64Url로 되어있기 때문에, 기본적으로 디코딩 가능 |
| Sign | HMAC-SHA256(<br>secret,<br>base64urlEncoding(header) + '.' +<br>base64urlEncoding(payload<br>)| secret key를 포함해 암호화되어 있음<br>Header에 대한 Base64Url를 적용한 값과 payload에 대한 Base64Url를 적용한 값들을 Header에 구성된 알고리즘으로 적용한 결과값 => secret key로 암호화 (비밀키는 서버측에 존재)<br>Header와 Payload 변조됐는지 검증 |

## 동작
![1](https://media.vlpt.us/images/ayoung0073/post/7a5b4ece-f295-47ec-bb2f-41a1a39b3574/image.png)
![2](https://media.vlpt.us/images/ayoung0073/post/cdb177a7-5844-49ae-bb3b-455c49958c11/image.png)

## JWT 장점 / 단점

### 장점
* 사용자 인증에 필요한 모든 정보는 토큰 자체에 포함 되어, 별도의 인증 저장소 필요 X
* 분산 마이크로 서비스 환경에서 중앙 집중식 인증 서버와 DB에 의존하지 않는 쉬운 인증 및 인가 방법 제공
* REST 서비스로 제공 가능
* URL 파라미터와 헤더로 사용
* 수평 스케일, 디버깅 및 관리 용이
* 트래픽에 대한 부담 낮음
* 독립적

### 단점(취약점)

JSON 웹 토큰은 세션 상태를 포함할 수 있다. 그러나 프로젝트 요건이 JWT 기간 만료 이전에 세션 무효화를 허용하는 경우 서비스는 더 이상 토큰만으로 토큰 표명(token assertion)을 신뢰할 수 없다.
 토큰에 저장된 세션이 폐지되지 않음을 확인하기 위해 토큰 표명은 데이터 스토어에 대해 검사되어야 한다. 
이렇게 하면 토큰이 더 이상 무상태가 아니게 됨으로써 JWT의 주된 이점이 약화되는 결과를 낳는다.

적절히 설계할 경우 개발자는 일부 주의를 기울이면 알고리즘 취약성을 해결할 수 있다

* JWT 헤더만으로 유효성을 확인하지 않을 것
* 알고리즘을 인지할 것
* 적절한 키 크기를 사용할 것


### 🧾Reference
1. [JSON 웹 토큰](https://ko.wikipedia.org/wiki/JSON_%EC%9B%B9_%ED%86%A0%ED%81%B0)
2. [JWT 구조](https://velog.io/@ayoung0073/springboot-JWT)
3. [spring-boot JWT 예제](https://sup2is.github.io/2020/03/05/spring-security-login-with-jwt.html)
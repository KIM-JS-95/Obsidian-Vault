---
layout: post
title:  "웹 보안을 강화하자"
date:   2022-02-08 12:05:21 +0800
tags: Spring-Security
color: rgb(154,133,255)
subtitle: Spring-Security CSRF
---

[[0-Spring-Security MOC.md]] · #spring/security <!-- moc-nav -->

 

## 🚀 스프링 시큐리티

스프링 환경은 정책에 따른 여러 `Spring-Security`가 공존할 수 있어 필터 Filter- Chain에 적용할 경우 충돌 문제가 생긴다.
때문에 Filter- Chain에 `Proxy`를 구성하여 시스템이 보안 상태를 동적으로 선택할 수 있도록 구성할 수 있다.


### 🍕 Authentication(인증)의 구조

![](https://gitlab.com/jongwons.choi/spring-boot-security-lecture/-/raw/master/images/fig-3-authentication.png)


### 🍕 CSRF(Cross-Site Request Forgery)

`CSRF`는 웹 애플리케이션의 취약점 중 하나로, 피해자가 의도하지 않는 요청을 통한 공격이다.

#### 🌠 Get 방식 공격 / Post 방식 공격

물론 공격자가 직접 `Get요청`을 보낼 수는 없다. 
공격자의 의도를 실현 하기 위해서는 피해자가 아래와 같은 요청을 보내도록 유도해야한다.

공격 방법으로는 Link/ Image 공격의 방식이 있다.


```commandline
    GET http://bank.com/trasnfer?accountNumber=5678&amount=10000
```

반면, `POST 요청`공격은 Image / Link 방식과는 다른 <form> 태그를 통한 공격을 시도한다.

```commandline
<form action="http://bank.com/transfer" method="POST">
    <input type="hidden" name="accountNumber" value="5678"/>
    <input type="hidden" name="amount" value="10000"/>
    <input type="submit" value="Pictures@"/>
</form>
```

#### 🌠 CSRF 방어?

> Our recommendation is to use CSRF protection for any request that could be processed by a browser by normal users. If you are only creating a service that is used by non-browser clients, you will likely want to disable CSRF protection.
>
> 일반 사용자가 브라우저를 통해 처리할 수 있는 모든 요청에 대해 CSRF 보호를 사용하는 것을 권장합니다.
> 
> 만약, 브라우저가 아닌 클라이언트에서 사용하는 서비스만 생성하는 경우 CSRF 보호를 비활성화 할 수 있습니다.
>
> -- Spring의 공식 문서 --

- 자격 증명이 유지
```
Rest API에서 토큰을 검색한 후에는 해당 토큰을 JS로 설정하여 브라우저 메모리에 저장한다.
토큰의 유효성은 현재 페이지에 대해서만 증명 가능한 토큰이다.

페이지 마다 토큰을 적용하기 때문에 가장 안전하지만 페이지를 새로고침 할때마다 다시 토큰을 부여해야한다.

때문에 잘 사용하지는 않는다.
```

- 브라우저 저장소에 저장된 자격 증명

```
브라우저 스토리지(예: 세션 스토리리)에서 토큰을 유지할 수 있다.
대표적으로 JWT를 사용하는 방법이 있다. 구현이 쉽고 코드가 브라우저 저장소에 접근하여 요청과 함께 토큰을 보낼 수 있다.
그러나 XSS 공격에 취약하다.
```

- 쿠키에 저장된 자격 증명

```
쿠기를 사용하여 자격 증명을 유지하는 방법으로 JWT와 같이 자격 증명만 유지할 수 있지만 사용자을 인증할 수는 없다.
REST API의 헤더를 통해 자격 증명을 읽는 방법이며 `토큰`은 Client가 소유하게 된다.
```

### 🍕REST API로 CSRF 보호 활성화


#### 🌠 Spring 구현

프로젝트에 CSRF 보호가 필요한 경우 사용자 지정 `WebSecurityConfigurerAdapter` 에서
`CookieCsrfTokenRepository` 를 사용하여 쿠키와 함께 CSRF 토큰을 보낼 수 있다 .

```java
@Configuration
public class SpringSecurityConfiguration extends WebSecurityConfigurerAdapter {
    @Override
    public void configure(HttpSecurity http) throws Exception {
        http
           .csrf()
                .csrfTokenRepository(CookieCsrfTokenRepository.withHttpOnlyFalse());
    }
}
```

#### 🌠 Client 구성

클라이언트 측 응용 프로그램에서 XSRF-TOKEN 쿠키는 첫 번째 API 액세스 후에 설정됩니다. JavaScript 정규식을 사용하여 검색할 수 있습니다.

```java
const csrfToken = document
        .cookie
        .replace(/(?:(?:^|.*;\s*)XSRF-TOKEN\s*\=\s*([^;]*).*$)|^.*$/, '$1');

fetch(url, {
method: 'POST',
body: JSON.stringify({ /* data to send */ }),
headers: { 'X-XSRF-TOKEN': csrfToken },
})
```

### 🍕 RoleHierarchy(권한계층)
최상위 권한 소유자가 모든 페이지 접근을 허용하는 방법?

#### 🌠 예시

모든 `ROLE_ADMIN`은 `ROLE_USER` 권한을 가질 수 있다.
```java

    @Bean
    RoleHierarchy roleHierarchy(){
          RoleHierarchyImpl roleHierarchy = new RoleHierarchy();
          roleHierarchy.setHierarchy("ROLE_ADMIN > ROLE_USER")
          return roleHierarchy;
    }
```

### 🧾 Reference

[CSRF](https://zzang9ha.tistory.com/341)

[Baeldung - CSRF With Stateless REST API](https://www.baeldung.com/csrf-stateless-rest-api)

[Servlet](https://mangkyu.tistory.com/14)
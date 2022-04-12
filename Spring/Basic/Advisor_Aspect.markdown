---
layout: post 
title:  "Spring AOP의 용어"
date:   2022-03-25 12:05:21 +0800 
tags: 스프링 
color: rgb(98,170,255)
subtitle: AOP
--- 

> 목차 <br>
> [AOP의 5가지 용어](#AOP의-5가지-용어)<br>
> [Advice 는 무었일까?](#Advice-는-무었일까?)<br>
> [Aspect는 정확이 무엇일까?](#Aspect는-정확이-무엇일까?)<br>
> [Advisor은?](#Advisor은?)<br>

 
## AOP의 5가지 용어

`AOP`를 학습했지만 아직도 모르는 어노테이션이 수두룩하다.

이번 포스팅에서는 `AOP`에서 가장 많이 사용되는 용어를 정리해 보려한다.

|용어|뜻|
|:---:|:---:|
|Aspect|관점, 측면|
|Advisor|조언자, 고문|
|Advice|조언, 충고|
|JoinPoint|결합점|
|Pointcut|자르는 점|


### Advice 는 무었일까?

충고라는 의미의 `Advice`는 `@Aspect` 를 가지는 class가 가지는 메소드이다.
다르게 말하면, **`pointcut`에 적용할 로직(메서드)를 의미한다.**

```java
@Aspect
@Component
public class ParameterAop {
    @Pointcut("execution(특정 클래스 혹은 메소드)")
    private void cut() {
    }

    @Before("cut()")
    public void before(Jointposint jointposint) {
    }

    @After(value = "cut()", returning = "object")
    public void after(Jointposint jointposint, Object object) {
    }
}
```

### Aspect는 정확이 무엇일까?

**`AOP`에서 Aspect는 여러 개의 Advice와 여러 개의 Pointcut의 결합체를 의미하는 용어이다.**

> Aspect = Advice들 + Pointcut들

### Advisor은?

조언자는 `Aspect`가 가지는 요소를 하나씩만 가지는 것으로 볼 수 있다.

> Advisor = 한 개의 Advice + 한 개의 Pointcut


그러나 스프링이 발전해 오면서 **다수의 Advice와 다수의 Pointcut을 다양하에 조합**해서 사용할 수 있는 `Aspect`의 등장으로
**하나의 Advice와 하나의 Pointcut만을 결합하는 Advisor를 사용할 필요가 없어졌기 때문이다.**


## Reference

- [한 번에 끝내는 Java/Spring 웹 개발 마스터 초격차 패키지 Online.]()
- [책 - 스프링을 입문을 위한 자바 객체 지향의 원리와 이해](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=55641908)

---
layout: post 
title: "Spring AOP 관점지향 프로그래밍"
date:  2022-03-25 12:05:21 +0800 
tags: 스프링 
color: rgb(98,170,255)
subtitle: AOP
--- 

> 목차 <br>
> [관점 지향 프로그래밍](#관점-지향-프로그래밍)<br>
> [횡단 관심사](#횡단-관심사)<br>
> [AOP 예제](#AOP-예제)<br>

 
## 관점 지향 프로그래밍

`관점`에 집중한 이 개념은 특수한 기능이 아닌 개발자가 하나의 로직에 집중할 수 있도록 별도의 로직을 개설하는 과정의 개념으로 볼 수 있다.

쉽게 **요리는 요리사가 미식은 미식가가 하는 것과 같은 것이다.** 

물론 미식가가 요리를 할 수 있지만 `먹는 행위`를 하는 것에 집중하는 것이 좋은 리뷰를 남길 수 있을 것이다.


비즈니스 개발에서는 다음과 같이 볼 수 있다.

`Spring Application`은 특별한 경우를 제외하고 MVC 웹 어플리케이션 에서는 `Web Layer` / `Business Layer` / `Data Layer`로 정의한다.

```
- Web Layer
    - REST API를 제공하며, Client 중심의 로직 적용

- Business Layer
    - 내부 정책에 따른 logic를 개발하며, 주로 해당 부분을 개발

- Data Layer
    - 데이터 베이스 및 외부와의 연동을 처리
```

`AOP`는 이러한 목표 아래 탄생한 개념인 것이다.

### 횡단 관심사

다수의 모듈에 공통적으로 나타나는 부분이 존재하며, 우리는 이것을 횡단 관심사 라고 말한다.

![029](https://user-images.githubusercontent.com/65659478/160230827-6d90b6ec-56fc-4dae-badc-5a2ac6c05262.jpg)

**이러한 관심사들 사이에 개발자가 목적을 가지고 임의적으로 코드를 주입할 수 있는데 여기서 등장하는 개념이 `AOP`인 것이다.**

> 스프링 DI가 의존성 주입이라면, 스프링 AOP는 로직의 주입이라고 볼 수 있다.
> 
>  <center>책, 스프링 입문을 위한 자바 객체 지향의 원리와 이해</center>

![030](https://user-images.githubusercontent.com/65659478/160230970-432ed18d-3d73-487b-9653-891d5d9e027b.jpg)

### AOP 예제

```java

//TODO: 관점 클래스 선언
@Aspect
@Component
public class ParameterAop {
    @Pointcut("execution(특정 클래스 혹은 메소드)")
    private void cut() {
    }

    @Before("cut()")
    public void before(Jointposint jointposint) {
        
        //TODO: 메소드 이름 출력 : 실행되는 메소드의 특정 지점을 찾아낼때 학인하는 방법 
        MethodSignature methodSignature = (MethodSignature)jointposint.getSignature();
        Method method = methodSignature.getMethod();
        System.out.println(method);
        
        //TODO: @Pointcut이 지정한 메소드가 실행되기 전에 현재 메소드가 실행됨
        Object[] args = jointposint.getArgs();

        for (Object obj : args) {
            System.out.println("before 메소드가 실행됩니다.");
            System.out.println("type: " + obj.getClass().getSimpleName());
            System.out.println("value: " + obj);
        }
    }

    @AfterReturning(value = "cut()", returning = "object")
    public void after(Jointposint jointposint, Object object) {
        //TODO: @Pointcut이 지정한 메소드가 실행된 이후 현재 메소드가 실행됨
        System.out.println("after 메소드가 실행됩니다.");
        System.out.println("return 오브젝트: ");
        System.out.println(object);
    }
}

@RestController
@RequestMapping("/api")
public class RestApiController {
    @GetMapping("/get/{id}")
    public String get(@PathVariable Long id, @RequestParam String name) {
        System.out.println("get method 실행!");
        return id + " " + name;
    }

    @PostMapping("/post")
    public User post(@RequestBody User user) {
        System.out.println("post method 실행!");
        return user;
    }
}
```




## Reference

- [책 - 스프링을 입문을 위한 자바 객체 지향의 원리와 이해](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=55641908)
- [한 번에 끝내는 Java/Spring 웹 개발 마스터 초격차 패키지 Online.]()
- [책 - 스프링을 입문을 위한 자바 객체 지향의 원리와 이해](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=55641908)
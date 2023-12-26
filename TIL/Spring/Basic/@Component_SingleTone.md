# @Configuration의 어노테이션은 SingleTon 이다.


## @Component 와 @Configuration 의 차이부터 알고 시작하자.

`@Component`는 스프링이 가지는 특징인 `DI`의 특성을 보여주는 어노테이션 일것이다.

이전까지 XML 파일에 개발자가 클래스 혹은 메소드를 `Bean`으로서 직접 주입해 주었다면 `@Component` 어노테이션의 등장으로
개발자가 직접 XML파일에 직접 작성하는 과정을 생략할 수 있었다.

스프링2.5 버전에서 추가된 이 버전은 @Controller, @Service, @Repository 어노테이션에 기본 내장되어있어
우리가 위 3가지를 클래스 상단에 추가해주기 때문에 `@Component` 를 선언 없이도 Bean으로서 사용할 수 있었던 것이다.

---
`@Configuration`은 어떨까?
스프링 3.0 에서 추가된 이 어노테이션 또한 메소드를 Bean으로서 자동 등록시켜주는 편리한 기능을 가지고 있다.

동일한 기능을 보이는 `@Component` 와 `@Configuration` 의 차이는 기반에서부터 차이를 보인다.
`@Component` 는 일반적인 스프링 빈을 나타내고, `@Configuration` 은 자바 기반의 스프링 구성 클래스를 나타낸다.
즉, 자바 기반으로 작성된 클래스의 경우 `@Configuration`를 설정하고 빈으로서 사용될 메소드에 `@Bean`을 추가하면
컨테이너에 주입하여 관리할 수 있는 것이다. 

또한 `@Configuration`은 `@Component`을 내장하고 있기 때문에 성격이 비슷한 것이다.


## @Configuration을 사용 해보자

```java
@Configuration
public class AnnotatedHelloConfig(){
    @Bean
    public AnnotatedHello annotatedHello(){
        return new AnnotatedHello();
    }
}

@Test
public void 테스트1(){
    // 컨텍스트 등록
    ApplicationContext ctx = 
            new AnnotationConfigApplicationContext(AnnotatedHelloConfig.class);
    // 등록된 컨텍스트 호출 
    AnnotationHelloConfig config 
            = ctx.getBean("annotationHelloConfig", AnnotatedHelloConfig.class);
    // 결과 1
    assertThat(config, is(notNullValue())); // True
    // 결과2
    assertThat(config.annotatedHello(), is(not(sameInstance(hello)))); // False
}
```

### 결과 1 확인
당연하지만 @Configuration을 통한 빈 등록은 성공적이다.

### 결과 2 확인
JAVA를 공부했다면 `new`를 통해 획득한 인스턴스 는 동일한 클래스라도 서로 다를 것이다.
그러나 결과 2에서 보여주듯 두 인스턴스는 동일함을 보여주는 테스트 결과를 보여준다.

## 호출된 메소드는 왜 동일한 인스턴스일까?
`@Bean`이 붙은 어노테이션이 annotatedHello() 메소드를 빈으로 생성할 때 가져갈 수 있는 정보는 무엇일까?

우리도 확인 할 수 있듯이 `클래스의 종류`, `메소드 이름` 이다. 
그리고 빈으로서 등록되기 위해서는 `메타 정보`가 필요하지만 정보가 없을 경우 디폴트 값으로 입력된다.

`@Configuration`으로 호출된 메소드가 동일한 인스턴스인 이유를 여기서 확인 할 수 있다.
스프링은 @Bean 애노테이션을 이용해 빈을 등록할 때 빈 메타정보를 `싱글톤(Singleton) 스코프`로 등록한다.

`Singleton`은 객체 지향 프로그래밍에서 디자인 패턴 중 하나로, 해당 클래스의 인스턴스가 오직 하나만 존재하도록 보장하는 패턴이다.
다시 말해, 2개 이상의 인스턴스의 생성이 불가능하며 한번 호출하면 동일한 인스턴스를 사용해야 하는 것이다.

## 어떻게 구분해서 사용할까?
JAVA 기반의 `@Configuration`은 Bean 스캐닝을 통한 인식으로는 등록하기 힘든 서비스 기능 혹은 컨테이너 XML 없이 등록하려고 할때
유용하게 쓰일 수 있다.
또한 싱글톤의 성격을 보여주기 때문에 역으로 생각한다면 **한번의 호출로 서비스 전역에서 사용할 수 있는 장점을 가진다.**

ChatGPT를 통해 해당 어노테이션의 사용 예시를 질문한 결과는 다음과 같다.

```
. 데이터베이스 연결 설정
데이터베이스 연결에 필요한 DataSource, EntityManagerFactory 등의 빈을 설정할 수 있습니다.

. 스프링 시큐리티 설정
스프링 시큐리티에서 필요한 빈들을 설정할 수 있습니다. 예를 들어, AuthenticationManager, UserDetailsService 등을 설정할 수 있습니다.

. 캐시 설정
스프링 캐시 추상화를 이용하여 캐시 설정을 할 수 있습니다. 예를 들어, EhCache, Redis 등의 캐시 구현체를 설정할 수 있습니다.

. 웹 애플리케이션 설정
스프링 웹 애플리케이션에서 필요한 빈들을 설정할 수 있습니다. 예를 들어, DispatcherServlet, HandlerMapping, ViewResolver 등을 설정할 수 있습니다.
```

그리고 `@Component`의 경우에는 다음과 같다.
```
. 서비스(Service) 클래스

. 리포지토리(Repository) 클래스

. 컨트롤러(Controller) 클래스
```

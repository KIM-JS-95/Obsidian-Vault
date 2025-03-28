# Spring WebFlux란?

`Spring WebFlux`는 Spring Framework 5에서 도입된 비동기 논블로킹(Asynchronous Non-blocking) 웹 프레임워크이다. 

기존의 `Spring MVC`가 동기 블로킹 방식으로 동작하는 것과 달리, WebFlux는 Reactive Streams를 기반으로 하여 높은 성능과 확장성을 제공합니다.

![](https://velog.velcdn.com/images/rnqhstlr2297/post/589794f6-95d1-42f1-920b-459cc4d26482/image.png)

## MVC와 WebFlux의 차이

| 특징                     | Spring MVC                          | Spring WebFlux                     |
|--------------------------|-------------------------------------|------------------------------------|
| **처리 방식**            | 동기 블로킹 (Synchronous Blocking) | 비동기 논블로킹 (Asynchronous Non-blocking) |
| **기반 아키텍처**        | Servlet API                        | Reactive Streams                   |
| **사용 기술**            | Tomcat, Jetty 등 Servlet 컨테이너  | Netty, Undertow 등 논블로킹 서버   |
| **적합한 사용 사례**     | 전통적인 웹 애플리케이션           | 실시간 데이터 처리, 고성능 애플리케이션 |
| **프로그래밍 모델**      | 명령형 프로그래밍                  | 함수형 프로그래밍                  |
| **확장성**               | 제한적                             | 높은 확장성                        |
| **리소스 사용 효율성**   | 낮음                               | 높음                               |

## 주요 특징
- **Reactive Streams 기반**: Reactor 프로젝트를 사용하여 Publisher, Subscriber 패턴을 구현.
- **비동기 논블로킹 I/O**: 효율적인 리소스 사용과 높은 처리량 제공.
- **함수형 프로그래밍 지원**: 함수형 스타일의 라우팅과 핸들러 정의 가능.
- **Netty 지원**: 기본적으로 Netty 서버를 사용하며, Servlet 3.1+ 컨테이너도 지원.

## 주요 구성 요소
- **Mono**: 0 또는 1개의 데이터를 처리하는 Publisher.
- **Flux**: 0개 이상의 데이터를 처리하는 Publisher.
- **WebClient**: 비동기 논블로킹 HTTP 클라이언트.

## 사용 사례
- 대규모 트래픽을 처리해야 하는 웹 애플리케이션.
- 실시간 데이터 스트리밍 서비스.

## 간단한 예시 코드

```java
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

// Mono
public class WebClientExample {
    public static void main(String[] args) {
        WebClient webClient = WebClient.create("https://jsonplaceholder.typicode.com");

        Mono<String> response = webClient.get()
                .uri("/posts/1")
                .retrieve()
                .bodyToMono(String.class);

        response.subscribe(System.out::println);
    }
}

// Flux
public class WebClientFluxExample {
    public static void main(String[] args) {
        WebClient webClient = WebClient.create("https://jsonplaceholder.typicode.com");

        Flux<String> responses = webClient.get()
                .uri("/posts")
                .retrieve()
                .bodyToFlux(String.class);

        responses.subscribe(System.out::println);
    }
}

```

### 코드 설명
1. **WebClient 생성**: `WebClient.create()` 메서드를 사용하여 기본 WebClient 인스턴스를 생성합니다.
2. **GET 요청**: `.get()` 메서드를 사용하여 HTTP GET 요청을 설정합니다.
3. **URI 설정**: `.uri()` 메서드를 통해 요청할 경로를 지정합니다.
4. **응답 처리**: `.retrieve()` 메서드를 사용하여 응답을 처리하고, `.bodyToMono(String.class)`로 응답 본문을 `Mono`로 변환합니다.
5. **구독**: `subscribe()` 메서드를 호출하여 데이터를 소비하고 결과를 출력합니다.


## 참고 자료
- [Spring WebFlux 공식 문서](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)
- [Reactor 프로젝트](https://projectreactor.io/)
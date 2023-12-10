---
layout: post
title:  "드디어 도착했다! Spring Cloud"
date:   2022-01-31 12:05:21 +0800
tags: Spring-Cloud
color: rgb(154,133,255)
subtitle: 서비스 기업의 기본 소양
--- 

## 🚀 Spring Cloud 서론

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FsjIkh%2Fbtq2x93djtb%2FrjHxNZM8IKXquIttp1WZKk%2Fimg.png)


```text

Spring Cloud is a framework for building robust cloud applications. The framework facilitates the development of applications by providing solutions to many of the common problems faced when moving to a distributed environment.

Applications that run with microservices architecture aim to simplify development, deployment, and maintenance. The decomposed nature of the application allows developers to focus on one problem at a time. Improvements can be introduced without impacting other parts of a system.

On the other hand, different challenges arise when we take on a microservice approach:

Externalizing configuration so that is flexible and does not require rebuild of the service on change
Service discovery
Hiding complexity of services deployed on different hosts
In this article, we'll build five microservices: a configuration server, a discovery server, a gateway server, a book service, and finally a rating service. These five microservices form a solid base application to begin cloud development and address the aforementioned challenges.


 - Baeldung 발췌 -
```
정리하자면 Spring Cloud는 클라우드 어플리케이션 구축 프레임 워크이며 
서비스 개발의 규모가 거대해지면서 각 서비스를 분산적으로 구축 및 개발 관리하는데 이를 `MSA(Micro Service Architecture)`라고한다.

서비스 역할 단위로 구분하여 개발하지만 서비스 이용시 하나의 서비스처럼 묶어 줄 수 있는 도구가 필요한데 여기서 등장하는 것이 `Spring Cloud`이다. 

### API GateWay

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcOMmF3%2Fbtq2ya2b5RT%2FF4BbSblKvvKLJBlxWiYZtK%2Fimg.png)

RESTful 하게 작성된 모든 서비스의 API를 손쉽게 관리하여 인증을 통한 자원의 효율적인 분배를 수행하는 기능이다.

즉, 클라이언트의 요청에 따라 적절한 서버에 찾아가도록 도와주는 서비스 이다.
반대로 말하면 API 통합 기술로 이를 사용하는 목적은 `서비스의 안정 과 집중 가능한 개발`

* 역할
  * 프록시의 역할과 로드밸런싱
  * 인증 서버로서의 기능
  * 로깅 서버로서의 기능

#### 종류
- Nginx
- Kong
- Apigee
- Spring Cloud Gateway(SCG)
- Spring Cloud Zuul
- AWS API Gateway


#### 장점

- 각각의 마이크로서비스들은 서로의 포트 번호를 몰라도 된다.
- Front 에서는 요청을 Gateway로만 보내면 되기 때문에 Gateway 포트만 알면 모든 요청을 수행할 수 있다.
- 모든 요청은 Gateway 를 거치기 때문에 로그를 쉽게 다룰 수 있다.
- Gateway 가 요청의 진입점이므로 통합 인증을 수행할 수 있다.

### Spring Cloud Netflix

`MSA`에서 요청에 따라 적절한 포트로 전송하기 위해서는 각 기능에 따른 포트 넘버를 알아야한다. 따라서 이를 관리해줄 도구가 필요한데 이를 `Service Discovery` 라고 한다.

대표적으로 사용되는 Discovery는 `Netflix OSS`에서 지원하는 `Eureka`이다


#### Netflix OSS
- Eureka : Discovery Server
  - 각각의 서비스 인스턴스들이 동적으로 확장, 축소 되더라도 인스턴스의 상태를 하나의 서비스로 관리할 수 있는 서비스


- Ribbon : Client Side Load Balancer
  - 부하 분산을 위한 모놀리스의 L4 스위치와 같이 트래픽을 분산시키는 기능


- Zuul : API Gateway
  - 각각의 마이크로서비스의 종단점을 연결하는 리버스 프록시


- Hystrix : Circuit Breaker
  - 특정 서비스가 과부하가 걸려 서비스 장애를 전파하는 특성을 해결하려는 기능


- EvCache
- Spectator
- Archaius


![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbgZcTF%2Fbtq3mgNS1qG%2Fliv97hmPLvbjFftavSkJIK%2Fimg.png)


### 🧾Reference
[Spring Cloud](https://www.baeldung.com/spring-cloud-configuration)

[Swegger 기본 사용법](https://leeys.tistory.com/29)

[Swagger Editor](https://editor.swagger.io/)

# 메세지 지향 미들웨어 (Message Oriented Middleware)

![](https://velog.velcdn.com/images/spamdong/post/cc902082-237d-453f-a254-c03027e63353/image.png)

메세지 지향 미들웨어(Message Oriented Middleware, MOM)는 분산 시스템에서 애플리케이션 간의 통신을 지원하는 소프트웨어 또는 하드웨어 인프라이다.

MOM은 `비동기 메시징`을 통해 애플리케이션 간의 데이터 교환을 가능하게 하며, `메시지 큐`를 사용하여 송신자(Publisher / Producer)와 수신자(Subscribe / Consumer) 간의 시간적 결합을 느슨하게 한다. 

이를 통해 시스템의 확장성과 유연성을 높일 수 있다.

## 메세지 큐

메세지 큐(Message Queue)는 비동기 통신을 지원하는 소프트웨어 엔지니어링 구성 요소로, 메시지를 임시로 저장하는 대기열이다. 

송신자가 메시지를 큐에 넣으면, 수신자는 큐에서 메시지를 꺼내 처리한다. 

이를 통해 송신자와 수신자는 동시에 실행될 필요가 없으며, 시스템의 유연성과 확장성을 높일 수 있다.

그러나 메세지 큐가 가용할 수 있는 용량이 한정적이기 때문에 메세지의 용량이 초과될 경우 메세지를 버리게 된다.

![](https://velog.velcdn.com/images/choidongkuen/post/b208dfbc-edd7-40ee-90b4-7fbd9f0f7166/image.png)

### 주요 특징
- **비동기성**: 송신자와 수신자가 동시에 실행되지 않아도 된다.
- **내구성**: 메시지는 큐에 안전하게 저장되어 손실되지 않는다.
- **확장성**: 시스템의 부하를 분산시켜 확장성을 높인다.
- **낮은 결합도**: 어플리케이션과 분리할 수 있다.

### 사용 사례
- **작업 분산**: 대규모 작업을 여러 개의 작은 작업으로 나누어 처리.
- **비동기 처리**: 사용자 요청에 대한 응답 시간을 줄이기 위해 비동기적으로 작업 처리.
- **시스템 통합**: 서로 다른 시스템 간의 데이터 교환을 원활하게 하기 위해 사용.

## 메세지 큐에서 데이터를 운반하는 방식

`메세지 브로커`와 `이벤트 브로커`는 시스템 간의 통신을 중재하는 역할을 하지만, 그 목적과 사용 방식에서 차이가 있다.

### 메세지 브로커 (Message Broker)
메세지 브로커는 주로 `메시지 큐`를 사용하여 송신자와 수신자 간의 메시지를 중재하는데 
메시지를 받아서 큐에 저장하고, 수신자가 준비되면 메시지를 전달한다.

이는 **비동기 통신을 가능하게 하며, 시스템의 결합도를 낮추는 데 유용합니다.**

- **예시**: RabbitMQ, ActiveMQ

- **특징**:
  - 메시지의 순서 보장
  - 메시지의 영구 저장
  - 여러 수신자에게 메시지 전달 가능 (팬아웃)

### 이벤트 브로커 (Event Broker)
이벤트 브로커는 이벤트 기반 아키텍처에서 사용된다.
이벤트를 발행하고 구독하는 방식으로 동작하며 이벤트는 상태 변화나 특정 액션을 나타내고 이벤트 브로커는 이러한 이벤트를 수신하여 구독자에게 전달합니다.

- **예시**: Apache Kafka, AWS SNS

- **특징**:
  - 이벤트 스트리밍
  - 실시간 데이터 처리
  - 이벤트의 순서 보장 (Kafka의 경우)

## 차이점 요약
- **메세지 브로커**는 주로 요청/응답 패턴을 지원하며, 메시지의 전달과 저장에 중점을 둡니다.
- **이벤트 브로커**는 이벤트 스트리밍과 실시간 데이터 처리를 지원하며, 이벤트의 발행/구독 패턴에 중점을 둡니다.
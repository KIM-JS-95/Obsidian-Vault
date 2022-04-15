---
layout: post 
title:  "Gradle 과 Maven 차이"
date:   2022-03-19 12:05:21 +0800 
tags: 면접 gradle maven
color: rgb(98,170,255)
subtitle: 빌트 툴에 대해 알아보자
--- 

## 빌드 관리 도구?

**빌드도구는 소스코드에서 어플리케이션 생성을 자동화 하기 위한 프로그램이다.** 

빌드는 코드를 사용 하거나 실행 가능한 형태로 `컴파일링`, `링킹`, `패키징` 하는것을 포함한다.

기본적으로 빌드 자동화는 아래와 같은 정형화된 다양한 작업을 스크립팅하거나 자동화 하는 행위이다

- 종속성 다운로드
- 소스코드를 바이너리코드로 컴파일
- 바이너리 코드를 패키징
- 테스트 실행
- 프로덕션 시스템에 배포

### Maven

- Maven은 **Java용 프로젝트 관리도구**로 `Apache의 Ant` 대안으로 만들어졌다.

- 빌드 중인 프로젝트, 빌드 순서, 다양한 외부 라이브러리 종속성 관계를 `pom.xml`파일에 명시한다.

- Maven은 외부저장소에서 필요한 라이브러리와 플러그인들을 다운로드 한다음, 로컬시스템의 캐시에 모두 저장한다.
  - 예를 들어, "Spring Boot Data JPA Starter" 모듈을 사용하여 프로젝트를 개발하고 싶다면 메이븐레포지토리에서 해당 모듈을 검색하여 xml 설정파일에 추가하여 사용할 수 있다. (참고로 maven용 코드 이외에도 gradle용 코드도 탭에 있다.)

### Gradle

`Gradle`은 Groovy를 이용한 빌드 자동화 시스템으로 현재 안드로이드 
앱을 만드는데 필요한 안드로이드 스튜디오의 공식 빌드 시스템이기도 하다.
Java, C/C++, 파이썬 등과 같은 여러 가지 언어를 지원한다.

- `Apacahe Maven`과 `Apache Ant`에서 볼수 있는 개념들을 사용하는 대안으로써 나온 프로젝트 빌드 관리 툴이다.(완전한 오픈소스)

- Groovy 언어를 사용한 `Domain-specific-language`를 사용한다. (간결한 코드가 장점)

- 꽤 큰규모로 예상되는 `multi-project` 빌드를 도울 수 있도록 디자인되었다.

- Gradle은 가독성이 좋아 프로젝트의 진행을 이해하기 쉽다.
- 
- 업데이트가 이미 반영된 빌드의 부분은 즉 더이상 재실행되지 않는다.

### Maven vs Gradle


## 🧾 Reference
- [빌드 도구란?](https://wangmin.tistory.com/50)
- [빌드 관리 도구 Maven과 Gradle 비교하기](https://jisooo.tistory.com/entry/Spring-%EB%B9%8C%EB%93%9C-%EA%B4%80%EB%A6%AC-%EB%8F%84%EA%B5%AC-Maven%EA%B3%BC-Gradle-%EB%B9%84%EA%B5%90%ED%95%98%EA%B8%B0)
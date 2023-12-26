---
layout: post 
title:  "객체지향설계의 5대 원칙 - SRP 편"
date:   2022-03-13 12:05:21 +0800 
tags: 면접 자바 SOLID
color: rgb(98,170,255)
subtitle: OOD 5대원칙
--- 

# 🚀 OOP를 올바르계 설계해 나가는 원칙
    
OOP의 4대 특성 `캡슐화`, `상속`, `추상화`, `다형성`은 객체지향 프로그래밍을 이어가는 동안 사용할 `Tool` 같은 역할이 된다.

도구가 있다면 용도에 맞게 사용해야하는데 요리를 하면 표준에 있듯이 OOP 세계에서도 원칙이라는 것이 존대한다.

`OOP`를 기반으로 설계하는 방식을 `OOD (Object Oriented Design)`이라고 하며 
설계 방법을 구체화 하여 정리한 원칙이 `SOLID`가 되는 것이다.

## 🌠  SOLID

원칙이 탄생한 것은 **높은 응집도와 낮은 결합도** 목표로 `로버트 C.마틴`이 확립한 개념이다.

### ☄ SRP(Single Responsibility Principle) : 단일 책임의 원칙

> "어떤 클래스를 변경해야 하는 이유는 오직 하나뿐이어야 한다."

![001](https://user-images.githubusercontent.com/65659478/158052296-f3c1ebf5-ef84-468b-b258-178f46957162.jpg)

하나의 클래스(남자)에 해야만 하는 역할이 너무다도 많다. 이 경우는 코드를 변경할 경우 복잡해지는 일이 발생할 것이다.

이 형태를 다음과 같이 바꾸면 그 역할히 더욱 이해하기 쉬워질 것이다.

![002](https://user-images.githubusercontent.com/65659478/158052294-4f8bbf14-c3a9-4835-ab19-c6c6bf4097c4.jpg)

이처럼 하나의 클래스에 `적합한 역할`을 구성하자는 원칙이 **단일 책임의 원칙**이 되는 것이다.

- 문제가 있는 코드

```java
public class 강아지 {
    final static Boolean 숫컷 = true;
    final static Boolean 암컷 = false;
    Boolean 성별;

    void 소변보다() {
        if (this.성별 == 숫컷) {
            // 한쪽 다리를 들고 소변을 본다.
        } else {
            // 뒤다리 두 개로 앉은 자세로 소변을 본다.
        }
    }
}
```

위 코드의 문제점을 찾아보면은 하나의 클래스에서 `소변보다()` 메소드가 암컷과 수컷의 행위를 모두 구현하는 것이 있다.

만일 더 많은 인스턴트가 존재할 경우 모든 변수에 대해 `if()`문을 구현한다면 코드는 **스파게티 코드** 가 될것이다.

**`SRP원칙`은 가정문을 사용하지 않고 클래스가 하나의 책임을 지는 것을 원칙으로 한다.**

- SRP 원칙을 확립한 코드

```java

public abstract class 강아지 {
    abstract void 소변보다();
}

public class 숫컷강아지 extends 강아지 {
	void 소변보다() {
		// 한쪽 다리를 들고 소변을 본다.
	}
}

public class 암컷강아지 extends 강아지 {
    void 소변보다() {
        // 뒤다리 두 개로 앉은 자세로 소변을 본다.
    }
}

```
개선된 코드는 `소변보다()`메소드를 클래스로 꺼내어 코드를 다루기 쉽도록 리팩토링하였다.


## 🧾 Reference
- [깃헙 - 스프링 입문 교재](https://github.com/expert0226/oopinspring)
- [책 - 스프링을 입문을 위한 자바 객체 지향의 원리와 이해](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=55641908)



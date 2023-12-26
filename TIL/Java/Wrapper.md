---
 
# 자바의 자료형 구분

![](http://wiki.hash.kr/images/thumb/4/45/Java_%EC%9E%90%EB%A3%8C%ED%98%95_%EB%B6%84%EB%A5%98.png/1400px-Java_%EC%9E%90%EB%A3%8C%ED%98%95_%EB%B6%84%EB%A5%98.png)

우리가 일반적으로 사용하는 `int`/ `long` 등의 타입은 `기본 자료형`에 속하는 타입이다. 

선언만 해준다면 값을 초기화 하여 바로바로 사용할 수 있었다.

만일 어떤 메소드에서 기본 자료형이 아닌 객체를 요구할 경우는 어떻게 해야할까? 

## 정수형 클래스의 필요성

```java
List<Object> list = new ArrayList<>();
```

우리는 List 에서 타입을 요구할 경우 Wrapper 타입을 요구하는 것을 이미 알고있다.

처음 `java.util` 패키지에서는 자료형을 요구할 경우 Object 타입의 값을 요구하고 있으며 우리는 그저 이유를 모르고 사용해왔던 것이었다.

자바에서 **OOP 4대 원칙 중 캡슐화** 는 외부에서는 접근을 제한하는 특성이 있다.

**이러한 원칙을 고수하여 많은 패키지들 또한 값을 안전하게 보호할 수 있는 Object 타입을 입력하도록 개발해 왔던 것일 것이다.**

### 때문에 필요한 정수 클래스

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FZolLT%2Fbtq8R0SHB75%2FIfszu8aary6ZEM8Jo6tANK%2Fimg.png
)
개발자들은 캡슐화 원칙에 따라 정수를 안전하게 보호할 수 있는 `Object`가 필요했다.
이러한 이유로 만들어진 것이 정수형 클래스 `Wrapper`인것이다.

### Boxing 과 UnBoxing

`Wrapper`은 포장이라는 뜻을 가지고 있다. 때문에 **기본타입 int를 포장하여 Integer로 선언한다. ** 라는 의미로 `Boxing` 이라고
그 반대가 `Unboxing`이게 되는 것이다.

Wrapper클래스는 캡슐화 특성에 따라 메소드를 통한 접근만이 허용되어 다음과 같은 접근만을 허용한다. 

```java
public class Wrapper_Ex {
    public static void main(String[] args)  {
        Integer num = new Integer(17); // 박싱
        int n = num.intValue(); //언박싱
        System.out.println(n);
    }
}
```

### 개발자들은 너무 귀찮았다. (🙋‍♂️라고 생각합니다.)

**그러나 오랜 시간 개발자들은 이러한 접근이 귀찮았는지 자동으로 Boxing / UnBoxing 되도록 수정해 내버린 것이다.**

그렇게 만들어진 것이 Auto Boxing / UnBoxing 방식인 것이다.

```java
public class Wrapper_Ex {
    public static void main(String[] args)  {
        Integer num = 17; // 자동 박싱
        int n = num; //자동 언박싱
        System.out.println(n);
    }
}
```

### Wrapper 클래스는 클래스 였던 것이다.!

**값을 비교한다라고 하면 우리는 연산자 `==`를 먼저 떠올릴 것이다.**

String 문자열을 비교한다면 어떨까?

수많은 알고리즘을 풀어보면서 String 타입은 연산자`==`를 사용하기보다 메서드`.equals()`를 사용해야한다는 것을 알았다. 

이유는 당연히 생각하지 않았다. 그저 **Object 니깐 사용한다.** 라고 생각해왔다.

그러나 정확한 이유는 `java.util 패키지`에 포함되어 있는 String 또한 하나의 클래스 였고 연산자 heap 영역에서 class는
참조값을 공유하므로 `.equals()`를 사용하는 것이 당연한 것이 었다.



## 정리

오랜 시간 개발자들은 자동방식의 자동 박싱 / 언박싱 방식에 익숙해 져버린 나머지 Wrapper 클래스의 필요성을 몰라왔던 것일지도 모른다.

그러나 `습관적`으로 사용해온 Wrapper 클래스는 우리 생활의 습관처럼 **이걸 왜 하는거지?** 라고 생각해온 것이라고 생각한다. 


## Reference
- [래퍼 클래스 - Wrapper Class](https://develop-im.tistory.com/m/81)

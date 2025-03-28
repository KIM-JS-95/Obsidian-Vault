# ThreadLocal이란?

`ThreadLocal`은 Java(ver.1.2)에서 제공하는 클래스 중 하나로, 각 스레드마다 독립적인 변수를 가질 수 있도록 지원한다. 

이를 통해 여러 스레드가 동시에 접근하더라도 서로 간섭 없이 데이터를 저장하고 사용할 수 있다.

## 주요 특징
- **스레드 독립성**: 각 스레드가 자신만의 값을 가지며, 다른 스레드와 값을 공유하지 않는다.

- **사용 목적**: 주로 스레드 간 공유가 필요 없는 데이터를 저장하거나, 스레드 컨텍스트를 유지하기 위해 사용

## 사용 예제
```java
public class ThreadLocalExample {
    private static ThreadLocal<Integer> threadLocal = ThreadLocal.withInitial(() -> 0);

    public static void main(String[] args) {
        Runnable task = () -> {
            int value = threadLocal.get();

            System.out.println(Thread.currentThread().getName() + " initial value: " + value);

            threadLocal.set(value + 1);

            System.out.println(Thread.currentThread().getName() + " updated value: " + threadLocal.get());
        };

        Thread thread1 = new Thread(task, "Thread-1");
        Thread thread2 = new Thread(task, "Thread-2");

        thread1.start();
        thread2.start();

        thread1.remove();
        thread2.remove();
    }
}
```

## 주의사항
- **메모리 누수**: `ThreadLocal`은 스레드가 종료되지 않으면 값이 계속 유지되므로, 사용 후 반드시 `remove()`를 호출하여 정리해야 한다.

- **적절한 사용**: `ThreadLocal`의 과도한 사용은 가독성과 유지보수성이 떨어질 수 있으니 특정 상황에서만 사용해야한다.

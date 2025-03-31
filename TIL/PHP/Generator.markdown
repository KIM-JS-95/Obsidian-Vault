# PHP 제너레이터 (Generator)

PHP 제너레이터는 `yield` 키워드를 사용하여 이터레이터를 쉽게 구현할 수 있도록 도와주는 기능이다.


## 장점
- 메모리 효율성: 큰 데이터 집합을 처리할 때 메모리를 절약할 수 있습니다.
- 코드 간결성: 반복자(iterator)를 직접 구현하는 것보다 간단합니다.
- 지연 실행(Lazy Evaluation): 필요한 시점에만 값을 생성합니다.

## 단점
- 제한된 기능: 제너레이터는 한 번만 순회할 수 있습니다. 다시 순회하려면 새로 생성해야 합니다.
- 디버깅 어려움: 제너레이터의 상태를 추적하는 것이 복잡할 수 있습니다.
- 복잡한 로직: 복잡한 데이터 흐름을 처리할 때 가독성이 떨어질 수 있습니다.

## 제너레이터의 기본 사용법

```php
<?php
function simpleGenerator() {
    yield 1;
    yield 2;
    yield 3;
}

foreach (simpleGenerator() as $value) {
    echo $value . PHP_EOL;
}
```

### 출력:
```
1
2
3
```

## 제너레이터의 장점
1. **메모리 효율성**: 모든 값을 한 번에 메모리에 로드하지 않고 필요할 때 생성합니다.
2. **코드 간결성**: 복잡한 이터레이터 클래스를 작성하지 않아도 됩니다.

## 키와 값을 함께 사용하는 제너레이터

```php
<?php
function keyValueGenerator() {
    yield 'a' => 'Apple';
    yield 'b' => 'Banana';
    yield 'c' => 'Cherry';
}

foreach (keyValueGenerator() as $key => $value) {
    echo "$key => $value" . PHP_EOL;
}
```

### 출력:
```
a => Apple
b => Banana
c => Cherry
```

## 제너레이터로 대량 데이터 처리

```php
<?php
function rangeGenerator($start, $end) {
    for ($i = $start; $i <= $end; $i++) {
        yield $i;
    }
}

foreach (rangeGenerator(1, 1000000) as $number) {
    if ($number % 100000 === 0) {
        echo $number . PHP_EOL;
    }
}
```

### 출력 (일부):
```
100000
200000
300000
...
1000000
```

위 예제는 메모리를 효율적으로 사용하여 1부터 1,000,000까지의 숫자를 생성합니다.

## 참고
- [PHP 공식 문서 - Generators](https://www.php.net/manual/en/language.generators.php)  
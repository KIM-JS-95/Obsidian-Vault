# PHP Interface

`Interface`는 클래스가 구현해야 하는 메서드의 청사진을 정의한다.
이를 통해 코드의 일관성을 유지하고, 서로 다른 클래스 간의 상호작용을 표준화가 가능하며
PHP에서 `interface` 키워드를 사용하여 인터페이스를 정의하게 된다.

### Interface의 주요 특징

- 인터페이스는 메서드의 시그니처만 정의하며, 구현은 하지 않는다.
- 클래스는 `implements` 키워드를 사용하여 인터페이스를 구현한다.
- 하나의 클래스는 여러 인터페이스를 구현할 수 있습니다.
- 인터페이스 내의 모든 메서드는 기본적으로 `public` 접근 제어자를 가집니다.


### 예제 코드
```php
interface Shape {
    public function getArea(): float;
}

class Circle implements Shape {
    private $radius;

    public function __construct(float $radius) {
        $this->radius = $radius;
    }

    // @Override
    public function getArea(): float {
        return pi() * $this->radius * $this->radius;
    }
}

class Rectangle implements Shape {
    private $width;
    private $height;

    public function __construct(float $width, float $height) {
        $this->width = $width;
        $this->height = $height;
    }

    public function getArea(): float {
        return $this->width * $this->height;
    }
}

$shapes = [
    new Circle(5),
    new Rectangle(4, 6)
];

foreach ($shapes as $shape) {
    echo "Area: " . $shape->getArea() . PHP_EOL;
}
```


## Generator Return Expressions
```php
<?php
$gen = (function() {
    yield 1;
    yield 2;

    return 3;
})();

foreach ($gen as $val) {
    echo $val, PHP_EOL;
}

echo $gen->getReturn(), PHP_EOL;
?>
```
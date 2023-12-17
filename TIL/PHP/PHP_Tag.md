# PHP 태그 의미

PHP를 다루다 보면 사람마다 php 의 시작을 알리는 `<? ?>` 의 사용 방법이 다르다는 것을 알 수 있다.

## 종류

|영어명|태그|설명|
|:---:|:---:|:---:|
|standard tag|<?php ?>|가장 기본적인 태그 형식|
|short open ta|<? ?>|기본값은 사용불가. short_open_tag=On 적용하면 사용가능. 권장하지 않음.|
|echo shortcut|<?= ?>|<?php echo 내용; ?>의 축약형|

## Sample

```php

// input
<?php $a = 'hello'; ?>
1: <?php echo $a; ?>
2: <? echo $a; ?>
3: <?= $a ?>

// outout
1: hello
2: <? echo $a; ?>
3: hello

```

## 정리
여러 문서를 통해 확인한 것은 `short_open_tag`를 사용할 것을 교육한다고 한다.

즉, 편리함을 위해 <?php ?> 보다는 <? ?>를 사용을 선호하는 유저가 많다는 의미인데

여러 커뮤니티에서는 XML 파일과 혼돈될 가능성을 두고 <u> 축약서 사용을 지양한다</u> 라고 말하고있다.


현재까지는 이미 오랜 시간 축약어를 사용해온 서비스를 위해 남겨두고 있다고는 하지만 이후 개발에서는 standard를 사용할 것을 권장하니

가급적이면 정석적인 길로 가도록 하자.


## reference
-[Deprecate short open tags, again](https://wiki.php.net/rfc/deprecate_php_short_tags_v2)
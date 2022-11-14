# str_replace vs strtr

## str_replace

문자열을 변경하지만 key 값을 기준으로 정의되어 여러 문자열이 변결될 수 있다.

```
<?php
$arrFrom = array("1","2","3","B");
$arrTo = array("A","B","C","D");
$word = "ZBB2";
echo str_replace($arrFrom, $arrTo, $word);
?>
```

`2`의 값이 `B`로 변경되어도 `B` 라는 key 값이 존재하기 때문에 키값에 대응하는 value 값을 호출하여 추가 변경하게된다.
process: "ZBB2" -> "ZDDB" -> "ZDDD"

expect: "ZDDB" but "ZDDD"


## strtr

`key` 값에 해단하는 단 하나의 값만 변경한다.

```
<?php
$arr = array("1" => "A","2" => "B","3" => "C","B" => "D");
$word = "ZBB2";
echo strtr($word,$arr);
?>
```

process: "ZBB2" -> "ZDDB"



# reference
-[stackoverflow](https://stackoverflow.com/questions/8177296/when-to-use-strtr-vs-str-replace)
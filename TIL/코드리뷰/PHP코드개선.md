# 기존 서비스의 코드를 개선해 보자

## PHP의 장점과 단점
PHP 언어의 가장 큰 장점은 무엇일까?

내 생각에는 SQL친화적이며 스크립트 언어로서 HTML 페이지와 함께 다루기 쉬운 언어라고 생각한다.

그렇다면 단점은 무엇일까?

개발자의 숙련도에 따라 다르겠지만

이번 프로젝트에서 내가 느낀 가장 불편했던 것은 과도하게 섞여있는 HTML과 PHP 코드일 것이다.

```html
<?
    $datas = getDatas(...);
    
    foreach($datas -> $v){
        echo `<div class="name"> 제 이름은 $v['name']` 입니다.`;
    } 
    ?>
    <input style="hidden" value ="1" name = "number">
    <?
    echo `<div class="name"> 제 이름은 $v['number']` 입니다.`;
?>
```

간단한 예시를 가져왔지만 내가 받게된 실제 사용중인 검색 서비스의 코드는 완벽한 `스파케티 코드`였고

간단한 코드 분석에도 이해하는 시간만 4일이 소요가 되었다.

또한 DB 접근을 위한 `Mysqli_connect()`의 과도한 사용으로 처리량이 과도했다.

```html
<?
for($i=0; $i<6; $i++){
    if($type =="main")
        $datas = getAllDatas(..., main);
    else
        $data = getSingleDatas(..., list);
    $cnt = getCount(...);
}
?>
```

시간 복잡도와 공간 복잡도를 고려한다면 `6*O(N)` 씩 2번의 과정이 발생한다.


## 목표

1. Html과 PHP 코드의 분리(단, AJAX를 사용하지 마세요. - 팀장 - )

   - 이때 살짝 어지러웠다.

2. DB 접근 코드 개선

### Html과 PHP 코드의 분리

이를 성공시키기 위해서는 `JavaScript`를 최대한 사용해야했다.

PHP코드 내부의 HTML코드를 최대한 걸러내고 JS가 처리를 대신하도록 설계했고
기능들을 메소드로 만들어 이후에도 코드의 가독성을 높였다.

```html
<?
    $datas = getDatas(...);
   
    foreach($datas -> $v){
        echo `<script src="javascript:getData(<?$v['name']?>)">`;
    } 
?>

<body>
    <div class="here"></div>

    <script>
    function getData(name){
        $(.here).append(name);
        }
    </script>
</body>
```

### DB 접근 코드 개선

```html
<?
for($i=0; $i<6; $i++){
    if($type =="main")
        $datas = getAllDatas(..., main);
    else
        $data = getSingleDatas(..., list);
    $cnt = getCount(...);
}
?>
```

Count 쿼리를 여러번 보낼 필요가 있을까?

여러차례 접근하여 데이터를 조회할 이유가 없었고 한번에 보내 처리하는 편이 부하를 줄일 수 있다 생각했다.

```html

<?
    $cnt = getAllCount(...);
    
for($i=0; $i<6; $i++){
    if($type =="main")
        $datas = getAllDatas(..., main);
    else
        $data = getSingleDatas(..., list);
}
?>
```

그러나 쿼리른 단순할 수록 빠른 속도를 가지는 SQL 특성상 하나의 쿼리에 여러번의 Count는 되려 속도가 느려지는 결과를
가져왔다.

```roomsql
select * from
(select count(id) from table1 ) as a
(select count(id) from table2 ) as b
(select count(id) from table3 ) as c
-- 처리시간 0.6 ~ 1s
```

해당 쿼리로 속도를 높일 수 있는 방법은 PHP와 Mysql의 API `Mysqli_multiquery` 기능을 사용해서 개선했다.

```
-- before
<?
   $q = "select * from
(select count(id) from table1 ) as a
(select count(id) from table2 ) as b
(select count(id) from table3 ) as c";
   
   $DB = Mysqli_connect(...);
   $result = $DB.queryExcute($q);
?>

-- after
<?
   $q = "select count(id) from table1 ";
   $q .= "select count(id) from table2 ";
   $q .= "select count(id) from table3 ";
   
   $DB = Mysqli_connect(...);
   $result = $Mysqli_MulqueryExcute($q);
?>
0.001 ~ 0.1s
```

## 결과

모든 서비스가 그렇듯 속도는 매우 중요하다. 

나의 첫 프로젝트는 실제 서비스를 위한 코드였고
사용자가 빠르게 써치하기 위해 쿼리와 데이터 로직을 고려하여 최소한의 처리시간으로 만들어야 했다.

취준 시절부터 좋은 개발자가 되기 위해
모든 코드라인에는 의문을 가지고 이유를 설명할 수 있어야 하며 

언제나 공간 복잡도와 시간복잡도를 생각하며 코드를 짜는 습관을 만들고 싶었고

한줄 한줄 고민하며 코드를 써 내려갔다. 

결과적으로 내 수준에서 좋은 코드 라인이 만들어 졌고 이후에도 관리하기 쉽도록 코드를 정리할 수 있었다.



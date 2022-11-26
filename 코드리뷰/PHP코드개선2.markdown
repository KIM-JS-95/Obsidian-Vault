# PHP 코드개선 2

## 목표
기존 json 스크립트를 요청사항에 맞게 가공하는 일이였지만 우리는 `토이 프로젝트` 가 아닌 실제 서비스에 적용될 업무였기 때문에

단순하게 설계하는 방법보다는 효율적으로 개발애햐만 했다.

>  요청사항
> 문자열 내부의 5~7개의 공백("\r\n") 기준으로 배열을 쪼개여 json 으로 반환할 것

## 가공 전
```json
{
  "category": "날씨",
  "content": "오늘 강원도 날씨는 ...       오늘 새벽 동해안에 강한 비바람 ...       미세먼지 주의 ..."
}
```

## 가공 후

```json
{
  "category": "날씨",
  "content": "오늘 강원도 날씨는 ...",
  
  "category": "날씨",
  "content":"오늘 새벽 동해안에 강한 비바람 ...",
  
  "category": "날씨",
  "content": "미세먼지 주의 ..."
}
```

## 내 방식

```php
<?
    
// [1] Mysql에서 데이터를 획득
    $ytnDB = new Mysql(" ... ");
    $rows = $ytnDB->querys(" ... ");
// [2] 데이터 array를 순회하면서 "날씨" 데이터에서 필요한 데이터를 $articles 변수에 저장한다.
    foreach($rows as $row){
        $temp = explode("\n", $row['content']);
        if(count($temp) < 10) continue;
        for($i=0;$i<count($temp);$i++){
                // 데이터를 1차 가공합니다.
                }
            }
            if($cnt>=$maxCnt) break;
        }
    }
    
// [3] $articles 변수를 while 문으로 순회하면서 공백 기준으로 데이터를 쪼개 json을 재구성한다.
    $k=0;
    while(true){
        $temp_len = count($articles);
        if(substr_count($articles[$k]['headline'],"       ")){
            $add = explode("       ", $articles[$k]['headline']);
            $articles = insert_array($articles, $k, $add);
            $k+=count($add);
        }
        $k++;
        if($temp_len<=$k) break;
    }
    
// * 배열을 쪼개 데이터를 삽입한다.
    function insert_array($arr, $idx, $add){        
        $arr_front = array_slice($arr, 0, $idx); //처음부터 해당 인덱스까지 자름
        $arr_end = array_slice($arr, $idx); //해당인덱스 부터 마지막까지 자름
        $arr_front[] = $add;//새 값 추가
        return array_merge($arr_front, $arr_end);
    }
?>
```

## 문제점

위 코드의 문제점을 확인하면
1. while
2. 시간 복잡도를 고려하지 않았다는 점 

초기 작업을 설계할 때에는 2가지로 프로세스로 구분하여 완성된 `array`를 다시 분해하는 과정을 선택했다.

때문에 시간 복잡도는 `2*O(n)`  과정을 이루기 때문에 좋은 코드는 못된것이다.

### while 사용이 왜 문제일까?

`for`과 `while` 의 작업 속도 차이의 문제가 아닌다.

많은 처리해야하는 데이터 즉, `INPUT 데이터`에 문제가 생길경우 while 문이 끝없이 반복된다면 어떨까?

기업이 사용하는 메인 서버에 과부하가 발생하여 서비스가 종료된다면 기업적 손해가 발생할 것이다.

기업적 손실을 생각한다면 완성도 높은 코드라도 while문 사용은 많은 고민을 해야할 것이다.

## 개선

`작업을 한큐에 끝낼것 / while 문을 사용하지 말것`

```PHP
<?
// [1] Mysql 에서 데이터를 획득
    $ytnDB = new Mysql(" ... ");
    $rows = $ytnDB->querys(" ... ");
// [2] 배열을 순회하면서 "날씨" 카테고리의 데이터를 $articles 변수에 저장한다.
    foreach($rows as $row){
        $temp = explode("\n", $row['content']);
        if(count($temp) < 10) continue;
        for($i=0;$i<count($temp);$i++){    
                        ...

                    if(trim($str1)=="날씨"){
                        if(substr_count($str2,"     ")){
                            $add = explode("     ", $str2);
                            /*
                             print_r($add);
                                Array
                                (
                                    [0] => 오늘 낮 동안 맑고 선선한 늦가을…밤사이 중서부 요란한 비
                                    [1] =>   늦은 오후∼내일 새벽, 중서부·전북 5mm 안팎 비…벼락·돌풍 동반
                                    [2] => 오후부터 중부 서해안·영동 강풍…안전사고 유의
                                )			
                            */
                            foreach($add as $s){
                                if(trim($s)!="") $articles[] = array("category"=>$str1, "headline"=>trim($s));
                            }
                        }else{
                        $articles[] = array("category"=>$str1, "headline"=>$str2);
                    }
                    $cnt++;
                    if($cnt>=$maxCnt) break;
                }
            }
            if($cnt>=$maxCnt) break;
        }
    }
?>
```

`insert_array function`을 제거하고 `$articles`을 생성하기 직전 데이터를 변환하는 작업을 추가하여
시간복잡도를 해결하고 조금도 직관적인 코드를 구성했다.


## 결론

별거아닌 문제도 초기 프로세스 설계에 접근방법이 잘못된다면
결과 코드는 크게 달라질 것이며 생산성 문제로 이어지게된다.

당시 `while 문`을 사용한 나는 30분동한 회사 서버를 마비시켰다.

`while 문이 쏘아올린 기업 손실` 인 것이다.

---

개발자로 일을 시작하는 사람들이 쉽게 빠지는 습관이 있다면 


`자신의 코드는 완벽하다.`는 오만과 

`지금 당장 작동하는 코드면 만족하는` 나태함 일것이다.


언제까지나 `나는 주니어 개발자니까`라는 안일한 마음으로 회사를 다닐 수는 없는 법이다.

그러니 어떤 일이 주어진다면 
잠시 키보드에서 손을때고 프로세스를 손으로 그리며 접근 방법을 설계하는 습관을 가지는 것이

코드 한줄보다 더 값진 경험을 가져가는 지름길이 아닐까?
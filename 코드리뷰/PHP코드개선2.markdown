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

```
<?
$maxCnt = 1000;
$cnt = 0;

$ytnDB = new Mysql(" ... ");
$rows = $ytnDB->querys(" ... ");
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

// 공백 기준으로 데이터를 쪼개 json을 재구성한다.
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

$ytnDB->close(); 
$json = array(
				  "editorId" => "Json",
				  "pubDate" => $row['n_date'],
				  "newsHeadLines" => $articles
				);
print_r($json); exit;

header("Content-Type: application/json; charset=UTF-8");
echo(json_encode($json, JSON_UNESCAPED_UNICODE));
?>
```

### 문제점

내가짠 코드에는 다양한 문제가 있지만 내가 말하고 싶은 문제점은 `while` 문을 사용했다는 점이다.
## 개선

```
<?
$maxCnt = 1000;
$cnt = 0;

$ytnDB = new Mysql("myDB");
$rows = $ytnDB->querys("select * from TBSVCS_SCROLL_MAIN_NEWS where agree_chk='1' order by idx desc limit 10");
foreach($rows as $row){
	$temp = explode("\n", $row['content']);
	// 데이터의 개수가 10개 이하라면 이전데이터를 가져온다
	if(count($temp) < 10) continue;
	for($i=0;$i<count($temp);$i++){
		$str1 = str_replace(" ", "", $temp[$i]);
		if(preg_match("/\*sc/", $str1) && !preg_match("/\*sc제보|\*sc편집전용주요뉴스|\*sc안내/", $str1) && !in_array($str1, $titleChk)){ 
			$titleChk[] = $str1;
			for($j=$i+1;$j<count($temp);$j++){
				if(trim($temp[$j])=="") continue;
				if(preg_match("/\*sc/", $temp[$j])){ $i=$j-1; break;}
				$str1 = str_replace("*sc", "", $str1); // 날씨
				$str2 = str_replace(array("=","\n"), "", $temp[$j]);
				$str3 = str_replace(" ", "", $str2); 
				if(trim($str1)=="날씨" && strstr($str3, "아침/낮(℃)")) continue;
				if(trim($str1)=="날씨"){
					if(substr_count($str2,"     ")){
						$add = explode("     ", $str2);
						/*
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
					}
				}else if(trim($str1)=="스포츠"){
					$add = explode("...", $str2);
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

//print_r($articles);
/*
$k=0;
$temp_len = count($articles);
while(true){
	if(substr_count($articles[$k]['headline'],"       ")){
		$add = explode("       ", $articles[$k]['headline']);
		$articles = insert_array($articles, $k, $add);
		$k+=count($add);
	}
	$k++;
	if($temp_len<=$k) break;
}
*/

$ytnDB->close(); 

$json = array(
				  "editorId" => "Json",
				  "pubDate" => $row['n_date'],
				  "newsHeadLines" => $articles
				);
print_r($json); exit;

header("Content-Type: application/json; charset=UTF-8");
//echo(json_encode($json, JSON_UNESCAPED_UNICODE));

?>
```
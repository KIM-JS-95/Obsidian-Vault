# PHP 코드개선 2

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
# 스핑크스 검색 문제 개선

`SPHINX` 검색 엔진이 가지는 가장 큰 문제는 노이즈 문제이다.

정확이 말하면 NGRAM이 가진 문제인데 검색 기능을 구현함에 있어서 노이즈 문제를 해결해야했다.


NGRAM에 대한 정확도를 높이기 위해서는 2가지 방법이있다.

1. N 의 수를 늘리자

2. TOKEN을 많이 가져가자 (검색 단어를 많이 입력하자)


ex) "산에서 들개"

의도) “<u>산에서 들개</u> 떼를 만났다” 등산 사고 민원 예고 울렸다...

결과) “<u>산에서 들개</u> 떼를 만났다” 등산 사고 민원 예고 울렸다...


BECK-END인 내가 할 수 있는 방법은 2번 방법이라고 생각했고 사용자가 의도한 정보를 획득하기 위해 검색결과가 저장된 Log를 분석하여 해결하고자 했다.

```
LOG 분석

1. 이용자는 문장보다 키워드를 많이 사용한다.
2. 키워드는 대부분 3가지를 넘지 않는다.
3. 각각의 사용자가 검색한 키워드의 흐름은 유사하다.

```

결국 사용자가 원하는 키워드 즉, 로그를 통해 사용자가 현재까지 가장 많이 검색한 키워드로 제안하여 토큰 수를 늘리는 것이 문제를 해결할 핵심이라고 생각했다.

```
시나리오

사용자의 검색 키워드 "우영우" > 로그 분석 > 가장 많이 검색한 키워드 "드라마 우영우"로 변환 > `SPHINX` 검색

```

그렇다면 분석은 어떻게 할것인가?

1. 키워드를 반드시 포함할 것
2. 다른 사용자들이 가장 많이 검색한 키워드를 기반으로 찾을 것


```php

	function expectN($input){
		$arr = [];
		$dateString = date("Ymd", time());
		$keyword=[];
		$keyword_cnt=[];

		// 당일로 부터 10일 이전까지의 모든 로그 기록을 획득
		for($i=10; $i>0; $i--){
			$date = mb_substr(date('Ymd', strtotime($dateString. ' - '.$i.'days')),2);
			array_push($arr,file("../../logs/zumSearchLog2-".$date.".log"));
		}

		$keylen = mb_strlen($input, "UTF-8");
		
		// 검색 기록 Filtering
		// sample > 날짜 || 검색어 || 사용자 IP 및 기기정보 || URL

		foreach($arr as $i => $days){
			foreach($days as $day){
			if(strpos(explode("||" ,$day)[1], $input)!==false){
				array_push($keyword, preg_replace("/(\"|\'|\\')/","", explode("||" ,$day)[1]));
				}
			}
		}
		
		// 검색 기록 Count 후 검색어와 유사하며 사용자가 많이 검색한 키워드 반환
		$keyword_cnt = array_count_values($keyword);

		$ans = 0;
		$index = 0;
		$key="";
		foreach($keyword_cnt as $i => $v){
			
			$temp = $v / $keylen;
			if($ans < $temp){
				$ans =$temp;
				$key = $index;
			}
			$index++;
		}

		return $input = $input > $keyword[$key] ? $input : $keyword[$key];
	}

```

# 해결하지 못한 문제

`max_inflix_len` 의 값을 변경하지 않고 ngram의 문제가 개선 될꺼라고는 생각되지 않는다.

"" 를 사용한 구문검색 이라도 "들개" 와 같은 <u>합성어</u>의 경우는 ngram이 작용하는 경우가 있다.

`stackOverFlow`에서 <u>구문검색의 `max_inflix_len` 적용에 대한 질문</u>을 던져도 어떠한 답변도 돌아오지 않았기 때문에

합성어 검색에 대한 문제를 어떡해 하면 개선할 수 있을지는 아직까지도 풀지 못하였다.



#REFERENCE
[ngram 단어예측](https://heytech.tistory.com/343)
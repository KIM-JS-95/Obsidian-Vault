# 서비스별 STT 개발 요구사항

## 요구사항
- 입력 데이터 확장자(.mp4)이며 자막은 확장성에 용이한 `VTT 형식`으로 관리한다.
- 서비스 업체 선택은 `API 지원 방식 / 문서화 / 비용` 3가지를 중심으로 체크 
- 결과 파일은 현재 사용중인 GS CDN에 저장하도록 하며 이후 파일을 관리할 수 있는 DB Table을 생성한다.

## 서비스별 요구사항
| 서비스          | AWS        | Naver Clova | AssemblyAI |
|----------------|------------|-------------|------------|
| PHP 지원 방식 | SDK        | cURL        | cURL       |
| 기타 언어      | PHP / JAVA / Python | PHP / JAVA / Python | PHP / JAVA / Python |
| 미디어 형식 지원 | Mp4 / mp3  | Mp4 / mp3   | Mp4 / mp3  |
| 화자분할       | O          | O           | O          |
| Input 링크     | S3 URI     | 접근가능 링크 | 접근가능 링크 |
| 출력           | VTT / SRT / JSON | SRT / JSON | VTT / SRT / JSON |
| 최대 용량     | 2GB / 4H   | 2GB / 2H    | 5GB /10H   |
| 비용(1분당)   | 0.024USD(32원) | 20원      | 0.006USD(8원) |
| 추가작업      | SRT -> VTT  |             | FFMPEG 오디오 작업 |
| 동기          | 비동기     | 동기 / 비동기 | 비동기     |


> - S3 URI: `s3://{bucket}/{file_name.mp4}`
> - sync: 인식 완료되면 response 결과(json)을 받을 수 있음
> - async: 입력한 Callback url 또는 ObjectStorage에 인식 결과를 리턴
> - 60초보다 긴 오디오를 텍스트로 변환하려면 데이터를 Google Cloud Storage 버킷에 저장


## 서비스별 처리시간
|        | 30초  | 1분25초 | 5분    | 12분    |
|--------|-------|----------|--------|---------|
| AWS    | 20s   | 31s      | 30s    | 61s     |
| Naver Clova | 4.7s | 5.9s   | 9.0s   | 측정불가 |
| AssemblyAI | 10.8s | 17.5s | 31.5s  | 75.4s   |


## 요금

### 2024.03 등록 영상 기준 (총 13,293분)

| 서비스       | 비용(분) | 총 비용   | 환산(24.03.22 기준) | 일평균(663분) | USD 환산 |
|--------------|----------|-----------|----------------------|---------------|----------|
| AWS          | 0.024USD | 319.032USD| 425,931원            | 21,277원      | 15.912USD|
| AssemblyAI   | 0.006USD | 79.758USD | 106,482원            | 5,316원       | 3.978USD |
| CLOVA        | - | 372,200원| -                    | ₩18,560원     | -        |
| GOOGLE       | 0.024USD | 319.032USD| 425,931원            | 21,277원      | 15.912USD|

### 2023.12 등록 영상 기준 (총 18409분)

| 서비스       | 비용(분) | 총 비용   | 환산(24.03.22 기준) | 일평균(594분) | USD 환산 |
|--------------|----------|-----------|----------------------|---------------|----------|
| AWS          | 0.024USD | 441.816USD| 592,070원            | 19,059원      | 14.256USD|
| AssemblyAI   | 0.006USD | 110.454USD| 148,017원           | 4,764원       | 3.564USD |
| CLOVA        | - | 515,450원| -                    | ₩16,630원     | -        |
| GOOGLE       | 0.024USD | 441.816USD| 592,070원            | 19,059원      | 14.256USD|



# 6. 개발

## AWS

### 개발 환경
AWS는 API 서비스 간에 높은 결합도를 보이는데, 이는 폐쇄성이 강하다고 말할 수 있다. 

특히나 AWS S3를 사용하지 않고 기업에서 외부 CDN 서버를 사용한다면 해당 서비스 이용에 있어 API 요청과 응답을 문제에 대해 생각 해야한다.


`AWS Transcribe`에 미디어 데이터 요청 시 S3 URI 값을 요구하는데, S3 bucket 생성과 데이터가 해당 Bucket에 저장되어 있어야 한다는 전제가 요구된다. 

또한 API 요청에 대한 결과 파일(VTT / SRT / JSON)이 S3 Bucket으로 떨어지기 때문에 해당 서비스가 AWS의 API 개발 환경이 폐쇄적이라고 느껴진 원인이 이것이다.


정리하면 API 요청 시 유저의 Access / Secret key를 요구하는데, 이는 IAM에 대한 정보이며 해당 IAM 권한에 `S3 Object Storage` / `AWS Transcribe`가 추가가 되어 있어야 사용할 수 있다.

![IAM이미지](/TIL/images/STT_IAM.png)

처리 방식은 sync / async 방식을 제공하며 요청 결과는 S3 에 저장된다. 

만일 외부 CDN을 사용하는 경우 결과 파일을 S3가 아닌 사용 중인 스토리지로 전달하는 작업이 필요하지만 
언제 작업이 완료될지 모르는 상황에서 지속적으로 작업 상태를 확인할 여유는 없을 것이고 cron_tab을 설정하자니 기업 입장에서는 등록 후 cron_tab이 동작하기를 마냥 기다릴 수는 없을 것이다.

API 성능은 다른 서비스와 비교할 수 없을 정도로 양호하지만 S3를 통한 데이터 교환만 가능하다는 점에서 기업에 적용하기란 쉽지 않을 것이다.


## Naver Clova

AWS와 다르게 네이버는 미디어 파일에 접근 가능 주소라면 어떤 방식이든 요청이 가능하며 응답으로 `Naver Object Storage`와 `CallBack`주소를 사용할 수 있다.

Request.php 파일에서 미디어 주소와 callback 주소를 기입하여 API를 요청하면 Response.php으로 요청시 기입한 파일 형태(JSON / SRT)로 return 해 주기 때문에 
이후 작업은 Response.php에서 처리해 줄 수 있다.

**외부CDN을 사용하는 기업 입장에서는 AWS를 대체할 수 있는 좋은 대안이 될 것이다.**

```PHP
<?php
 $audio_url ='{Your media URL can access}';
 $response = req_url($audio_url, 'async');
 
 function req_url($url, $completion){
     $object = (object)[
         'language' => 'ko-KR',
         'completion' => $completion,
         'url' => $url,
 		'diarization.enable'=>false,
 		'resultToObs'=>false,
 		'format'=>'JSON'
 	    	'callback'=>'https://{your_domain}/clova_callback.php',
 		// Add parameters If you want
 		// 'callback' => 'https://{your domain}/clova_callback.php?name=Jhon_mike'
     ];
     return execute('/recognizer/url', $object);
 }
 
 
 function execute($uri, $object){
   $secret = '{Clova_secret}';
   $invoke_url = '{Clova_secret}';
   
     try {
         $ch = curl_init($invoke_url . $uri);
         curl_setopt($ch, CURLOPT_POST, true);
         curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
         curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
         curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'POST');
         curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($object));
         curl_setopt($ch, CURLOPT_VERBOSE, true);
         curl_setopt($ch, CURLOPT_TIMEOUT, 600);
         
 		    $headers = ['Content-Type: application/json', 'X-CLOVASPEECH-API-KEY: ' . $secret];
         curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
       
         $response = curl_exec($ch);
         $err = curl_error($ch);
         curl_close($ch);
 
         if ($err) {
             echo 'cURL Error #:' . $err;
             return $err;
         }
         return $response;
     } catch (Exception $E) {
         echo 'Response: ' . $E . '\n';
         return $E->lastResponse;
     }
 }
?>
```
[gitgubgist - clova_callback.php](https://gist.github.com/KIM-JS-95/da74938d985bebc40bbeb9f4b86c68da)


```PHP
<?
$name = $_GET['name']; // Jhon_mike
$jsonData = file_get_contents('php://input');
$response = json_decode($response, true);
$transcript_id = $response["token"];

if($response['result'] == 'COMPLETED'){
	$vtt_content = json_to_vtt($response);
	$storate_dir = "transcription/".date("Y/m");
	$filename=buffer_upFtp($transcript_id, $storate_dir, $vtt_content , ".vtt");
}else{
	$mgs = "Transcript Not Complete.";
	STT_WriteLog($transcript_id, $mgs);
	exit;
}

function json_to_vtt($json_data) {
	$segments = $json_data["segments"];
	$vtt_content = "WEBVTT\n\n";

	foreach ($segments as $index => $segment) {
		$start_time = $segment["start"] / 1000;
		$end_time = $segment["end"] / 1000;
		$text = $segment["text"];

		$start_time_str = format_time($start_time);
		$end_time_str = format_time($end_time);

		$vtt_content .= $index + 1 . "\n";
		$vtt_content .= $start_time_str . " --> " . $end_time_str . "\n";
		$vtt_content .= $text . "\n\n";
	}

	return $vtt_content;
}

function format_time($seconds) {
	$hours = floor($seconds / 3600);
	$seconds %= 3600;
	$minutes = floor($seconds / 60);
	$seconds %= 60;
	$milliseconds = ($seconds - floor($seconds)) * 1000;
	return sprintf("%02d:%02d:%02d.%03d", $hours, $minutes, floor($seconds), $milliseconds);
}

function buffer_upFtp($token, $storate_dir, $file_buffer, $type){
	global $_SE;
	try{
		$client=connectS3($_SE['script']);
		$rst = $client->putObject([
			'Bucket' => "mobile",
			'Key' => '<Your save S3_ROOT>',
			'ContentType' => $type,
			'Body' => $file_buffer,
		]);
	}catch (Exception $e){
		$msg = $e->getMessage();
		STT_WriteLog($token, $msg);
		return false;
	}
	return true;
}

/// Add function what you want ....
?>
```
[gitgubgist - clova_transcribe.php](https://gist.github.com/KIM-JS-95/175f62d2b72fabf786f42c02b5955503)

## AssemblyAI

STT(Speech to Text)에 집중하여 개발하는 AI스타트업으로 높은 정확도와 저렴한 비용을 자랑한다.

webhooks(callback 기능과 동일)을 지원하여 **외부 CDN을 사용하는 기업 입장에서는 Naver_Clova다음으로 좋은 대안이 될 것이다.** 


JAVA, Python, Ruby, GO, PHP 코드를 사용할 수 있는 자체 API를 운용과 문서도 제공하고 있어 어렵지 않게 코드작성을 할 수 있다.

 
PHP의 경우 Webhooks 요청은 body에 적으면 요청할 수 있다. 
**(API 문서에는 찾을 수 없으니 참고)**

```PHP
<?php
/*-----------------------------------------------------------------------------------------
	- 이름 : assemblyAI_transcribe.php
	- Reference Site:
		[assemblyAI]: https://www.assemblyai.com/
		[webhook]: https://www.assemblyai.com/docs/getting-started/webhooks
-----------------------------------------------------------------------------------------*/

$audio_url ="{accessible media doamain}";

// 1. 자막생성
$transcript_id = createSubtitle($audio_url);

function createSubtitle($audio_url){
	$headers = array(
		"authorization: ".'{assembly_key}',  // AssemblyAI API key
		"content-type: application/json"
	);

	$data = array(
		"audio_url" => $audio_url,
		"language_code"=>"ko",
		'webhook_url' => 'https://{your domain}/assemblyAI_callback.php'
		// Add parameters If you want
		// 'webhook_url' => 'https://{your domain}/assemblyAI_callback.php'?name=Jhon_mike
	);

	$transcript_endpoint = "https://api.assemblyai.com/v2/transcript";
	$curl = curl_init($transcript_endpoint);
	curl_setopt($curl, CURLOPT_POST, true);
	curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode($data));
	curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
	curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

	$response = curl_exec($curl);
	$response = json_decode($response, true);
	curl_close($curl);
	return $response['id'];
}
?>
```

[gitgubgist - assemblyAI_transcribe.php](https://gist.github.com/KIM-JS-95/41c440181cc566d48d412ddadeb85f1e)

```PHP
<?
$name = $_GET['name']; // Jhon_mike
$jsonData = file_get_contents('php://input');
$json_data = json_decode($jsonData, true);

if($json_data["status"]="completed"){
	$transcript_id = $json_data['transcript_id'];
	$response = getSubtitleFile($transcript_id);

	if(preg_match('/^WEBVTT/i', $response)){
		$storate_dir = "/transcription/".date("Y/m");
		$filename=buffer_upFtp($transcript_id, $storate_dir, $response,".vtt");
	}else{
		$response = json_decode($response, true);
		$mgs = $response['error'];
		STT_WriteLog($transcript_id, $mgs);
		return false;
	}
	return true;

}else{
	STT_WriteLog($transcript_id, "{$json_data['error']}");
	return false;
}

function getSubtitleFile($transcript_id, $fileFormat='vtt'){
	global $_SE;

	$headers = array(
		"authorization: ".$_SE['assembly_key'],
		"content-type: application/json"
	);

    $url = "https://api.assemblyai.com/v2/transcript/{$transcript_id}/vtt";
    $curl = curl_init();
    curl_setopt_array($curl, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER => $headers
    ]);

    $response = curl_exec($curl); // 성공 -> vtt / 실패 -> json
	curl_close($curl);

	return $response;
}

function buffer_upFtp($token, $storate_dir, $file_buffer, $type){
	global $_SE;
	$_FILES_NAME = $token.$type;
	try{
		$client=connectS3($_SE['script']);
		$rst = $client->putObject([
			'Bucket' => "mobile",
			'Key' => '{Your save S3_Root}'.$_FILES_NAME,
			'ContentType' => $type,
			'Body' => $file_buffer,
		]);
	}catch (Exception $e){
		$msg = $e->getMessage();
		STT_WriteLog($token, $msg);
		return false;
	}
	return true;
}
?>
```
(gitgubgist - assemblyAI_callback.php)[https://gist.github.com/KIM-JS-95/5a037ea401bcb4b95764d706db7d8c0b]

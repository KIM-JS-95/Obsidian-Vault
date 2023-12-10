# AJAX vs CURL

## 원문
cURL is a server-side process. 
This means that it will be called before the page is rendered and has nothing to do with the client's capabilities.

AJAX, however, is a client-side call. 
This means that it will not be executed until the client loads the page 
(or at least that piece of code is seen and executed, but this typically works on document.ready).

If you're looking to retrieve the information and dump it to the user immediately then cURL is your best bet. 
If you'd like to do a progressive load (dump the page, then retrieve the content for a "seamless" load to the user) 
then AJAX is the best bet. All th while keep in mind, though in today's day and age it's semi trivial,
AJAX may be disabled in cases of FireFox's NoScript extension.

That being said, the source of the cURL execution will be on the server. 
The source of the AJAX request will be on a per-client basis. Neither of which provide a secure means of detection 
(server-side) to know who sent what (as headers can be altered).


## 기본부터 알고 가자

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FDklcb%2FbtrmALodDSf%2F1sFiV7OwIjU4207SKia3Q0%2Fimg.png)

AJAX는 `클라이언트 사이드`의 호출 방식이며 자바스크립트 기반으로 서버와 통신을 하기 위한 비동기 통신방법이다.

cURL(client-URL)은 C언어 기반의 `data transfer tool` 로서 라이브러리 형태로 제공된다.

또한 `서버 사이드` 호출을 기반으로 `커맨드 라인환경(SHELL)`에서 또한 사용할 수 있어 환경에 상관없이 사용이 가능하다.

## cURL 사용가능 언어
`서버 사이드` 통신 방식의 cURL은 이에 대응하여 서버 사이드 스크립트 언어(PHP, JAVA, Python 등)에서 사용 가능하다.

순수 JS는 클라이언스 스크립트언어도 AJAX 통신 방법을 가지고 있지만 

Node.js 런타임 엔진을 사용하여 서버 사이드를 구축한다면 cURL을 사용할 수도 있을 것이다.

### cURL은 비동기 통신이 가능할까?

AJAX는 이름부터 비동기의 성격을 지니고 있지만 
공식 페이지에도 cURL 비동기에 대한 정보가 없으며 `cURL async`라고 검색하면 프로세스를 병렬처리하는 `parallel(php 에서는 curl_multi)` 함수만 있을 뿐
이것이 정말 비동기 통신이라고 볼 수는 없을 것이다.

```shell
mycurl() {
    START=$(date +%s)
    curl -s "http://some_url_here/"$1  > $1.txt
    END=$(date +%s)
    DIFF=$(( $END - $START ))
    echo "It took $DIFF seconds"
}
export -f mycurl

seq 100000 | parallel -j0 mycurl
```

PHP 에서 통신을 위해서는 cURL 사용이 일반적이지만 이 또한 비동기 통신은 아니다.
이를 극복하기 위해 스레드를 늘리거나 소켓을 개방하는 다양한 방법을 사용하고있다.

물론 php 프레임워크(codeIgniter, Laravel)에서는 비동기를 지원하는 듯 하다.



# reference
- [AJAX vs CURL stackoverflow](https://stackoverflow.com/questions/4775592/ajax-versus-curl)
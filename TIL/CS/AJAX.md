# AJAX(Asynchronous JavaScript and XML)

Ajax는 빠르게 동작하는 동적인 웹 페이지를 만들기 위한 개발 기법 중 하나

Ajax는 웹 페이지 전체를 다시 로딩하지 않고도, 웹 페이지의 일부분만을 갱신할 수 있다.

즉 Ajax를 이용하면 백그라운드 영역에서 서버와 통신하여, 그 결과를 웹 페이지의 일부분에만 표시할 수 있다.

## AJAX 장점

1. 웹 페이지 전체를 다시 로딩하지 않고도, 웹 페이지의 일부분만을 갱신할 수 있다.
2. 웹 페이지가 로드된 후에 서버로 데이터 요청을 보낼 수 있다.
3. 웹 페이지가 로드된 후에 서버로부터 데이터를 받을 수 있다.
4. 백그라운드 영역에서 서버로 데이터를 보낼 수 있다.

## Ajax의 한계

1. Ajax는 클라이언트가 서버에 데이터를 요청하는 `클라이언트 풀링 방식`을 사용하므로, 서버 푸시 방식의 실시간 서비스는 만들 수 없다.
2. Ajax로는 바이너리 데이터를 보내거나 받을 수 없다.
3. Ajax 스크립트가 포함된 서버가 아닌 다른 서버로 Ajax 요청을 보낼 수는 없다.
4. 클라이언트의 PC로 Ajax 요청을 보낼 수는 없다.
  

## 동작원리

Ajax는 기존에 사용되던 여러 기술을 함께 사용하여, 웹 페이지의 **일부분만을 갱신할 수 있도록 해주는 개발 기법이다.**

이러한 Ajax에서 사용하는 기존 기술은 다음과 같다.

- 웹 페이지의 표현을 위한 HTML과 CSS
- 데이터에 접근하거나 화면 구성을 동적으로 조작하기 위해 사용되는 DOM 모델
- 데이터의 교환을 위한 JSON이나 XML
- 웹 서버와의 비동기식 통신을 위한 XMLHttpRequest 객체
- 위에서 언급한 모든 기술을 결합하여 사용자의 작업 흐름을 제어하는 데 사용되는 <u>자바스크립트</u>


![1](https://blog.kakaocdn.net/dn/DpRtq/btrWwgyQzum/THLCYe64HkKZAywMIOKrJ0/img.png)


## Ajax 메소드

[ajax 상세 메소드 리스트](https://www.tutorialsteacher.com/jquery/jquery-ajax-method)

1) Ajax 메소드

| method | 설명 |
|:---:|:---:|
| $.ajax() | 비동기식 Ajax를 이용하여 HTTP 요청을 전송함. |
| $.get() | 전달받은 주소로 GET 방식의 HTTP 요청을 전송함. |
| $.post() | 전달받은 주소로 POST 방식의 HTTP 요청을 전송함. |
| $.getScript() | 웹 페이지에 스크립트를 추가함. |
| $.getJSON() | 전달받은 주소로 GET 방식의 HTTP 요청을 전송하여, 응답으로 JSON 파일을 전송받음. |
| .load() | 서버에서 데이터를 읽은 후, 읽어 들인 HTML 코드를 선택한 요소에 배치함. |


2) 메소드 체이닝(method chaining)

| method | 설명 |
|:---:|:---:|
| done | HTTP 요청이 성공하면 요청한 데이터가 done() 메소드로 전달된다. |
| fail | HTTP 요청이 실패하면 오류와 상태에 관한 정보가 fail() 메소드로 전달된다. |
| always | HTTP 요청이 성공하거나 실패하는 것에 상관없이 언제나 always() 메소드가 실행된다. |


3) 예시
```
var main = {
    init : function () {
        var _this = this;
        $('#btn-save').on('click', function () {
            _this.save();
        });
    },
    
    save : function () {
        var data = {
            title: $('#title').val(),
            author: $('#author').val(),
            content: $('#content').val()
        };

        $.ajax({
            type: 'POST',
            url: '/api/v1/posts',
            dataType: 'json',
            contentType:'application/json; charset=utf-8',
            data: JSON.stringify(data)
        }).done(function() {
            alert('글이 등록되었습니다.');
            window.location.href = '/';
        }).fail(function (error) {
            alert(JSON.stringify(error));
        });
    },
    

};

main.init();

```
http에서의 특정 요소에 접근하기 위해 *DOM*을 사용하여 버튼에 대한 js 변수를 선언후 해당 Object에 접근하도록 명령어를 구성한다.

var data= {}; 는 게시판 글 작성시 작성된 데이터 객체를 각 변수에 저장하고 하나의 Array 변수 'data' 에 저장하여 ajax {data: (data)} 형식으로 

전송하게된다.


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

공식 페이지에도 cURL 비동기에 대한 정보가 없으며 `cURL async`라고 검색하면 프로세스를 병렬처리하는 `parallel(php 에서는 curl_multi)` 함수에 대한 정보가 있지만
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

# reference
- [AJAX vs CURL stackoverflow](https://stackoverflow.com/questions/4775592/ajax-versus-curl)

### 🧾Reference
- [Ajax 기초](http://tcpschool.com/ajax/ajax_intro_basic)
- [Ajax 상세](http://tcpschool.com/jquery/jq_ajax_method)

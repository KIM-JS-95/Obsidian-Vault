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

![동작원리](http://tcpschool.com/lectures/img_ajax_ajax_application.png) 
![동작원리](http://tcpschool.com/lectures/img_ajax_other_application.png)


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

| 오후 | 저녁 |
|:---:|:---:|
| 13:00 ~ 17:00 | 11:00 ~ 02:00 |

### 🧾Reference
- [Ajax 기초](http://tcpschool.com/ajax/ajax_intro_basic)
- [Ajax 상세](http://tcpschool.com/jquery/jq_ajax_method)

# PHP 팝업 구현

popup 창을 통해 추가 html, 이미지 등 다양한 파일을 호출한다.

이는 `$_SESSION` 보다 가벼운 `$_COOKIE`를 사용하는 것이 바람직하다.

또한 파일은 서버에 저장된 파일을 호출하는 방식이기때문에 추가 팝업 파일을 만들어 두어야한다.

## 팝업창 호출

팝업창을 호출하기 위해 JS파일을 만들어 쿠키를 핸들링 하도록 하였다.

```js
// popup_opener.js

function getCookie( name )
{
  var nameOfCookie = name + "=";
  var x = 0;
  while ( x <= document.cookie.length ) {
  var y = (x+nameOfCookie.length);
  if ( document.cookie.substring( x, y ) == nameOfCookie ) {
  if ( (endOfCookie=document.cookie.indexOf( ";", y )) == -1 )
  endOfCookie = document.cookie.length;
  return unescape( document.cookie.substring( y, endOfCookie ) ); }
  x = document.cookie.indexOf( " ", x ) + 1;
  if ( x == 0 )
  break; }
  return "";
}


var dt = new Date();

// date && time set
var str = dt.getFullYear()+("00"+(dt.getMonth()+1)).slice(-2)+("00"+dt.getDate()).slice(-2)+("00"+dt.getHours()).slice(-2)+("00"+dt.getMinutes()).slice(-2);

// 유효기간이 필요한 경우 str변수에 대한 범위를 지정하도록 한다.
if ( getCookie( "popup221026" ) != "done" && str>="202210260900" && str<"202211080000")
{
	noticeWindow1 = window.open('팝업 파일','팝업 창 이름','팝업창 옵션');
	noticeWindow1.opener = self;
}

```


## 오늘 하루 이창을 열지 않기

쿠키 만료시간을 특정하여 지정할 수 있다.

현재 사용되는 쿠키값을 `현재 날짜 + 1D`로 변경하여 수정하면 된다.

```php
function setCookie(cookiename, value, expiredays){
	var todayDate = new Date();
	todayDate.setDate(todayDate.getDate() + expiredays);
	document.cookie = cookiename + "=done; path=/; expires=" + todayDate.toGMTString() +1+ ";";
}

function closeToday(no){
	setCookie("cookie_name","1",1);
	self.close();
}
```

## 팝업 html

```php

// popup_target.php

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-Transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>title</title>
<style type="text/css">img{border:0}html{overflow:hidden}*{padding:0;margin:0}</style>
<script type="text/javascript" src="../_js/jquery.min.js"></script>
<script type="text/javascript">
//팝업사이즈 자동조절
$(window).load(function() {
	var strWidth;
	var strHeight;

	//innerWidth / innerHeight / outerWidth / outerHeight 지원 브라우저
	if(window.innerWidth && window.innerHeight && window.outerWidth && window.outerHeight){
		strWidth = $('#contents').outerWidth() + (window.outerWidth - window.innerWidth);
		strHeight = $('#contents').outerHeight() + (window.outerHeight - window.innerHeight);
	}
	else{
		var strDocumentWidth = $(document).outerWidth();
		var strDocumentHeight = $(document).outerHeight();

		window.resizeTo(strDocumentWidth, strDocumentHeight);

		var strMenuWidth = strDocumentWidth - $(window).width();
		var strMenuHeight = strDocumentHeight - $(window).height();

		strWidth = $('#contents').outerWidth() + strMenuWidth;
		strHeight = $('#contents').outerHeight() + strMenuHeight;
	}

	//resize
	window.resizeTo( strWidth, strHeight );
});

function setCookie(cookiename, value, expiredays)
{
	var todayDate = new Date();
	todayDate.setDate(todayDate.getDate() + expiredays);
	document.cookie = cookiename + "=done; path=/; expires=" + todayDate.toGMTString() +1+ ";";
}
function closeToday(no)
{
	setCookie("cookie_name","1",1);
	self.close();
}


function popMove(){ //링크 있을시
    if(opener.parent.noticeWindow1){
	    opener.parent.noticeWindow1.close();
    }
    opener.location.href = "your_link";
    self.close();
}


</script>
<body>
<form name="open">
<div id="contents" style="width:550px;margin:0;padding:0;">
	<img src="호출할 파일 링크" width="550" height="341">
	<div style="height:25px;background-color:#000;font:12px dotum;color:#fff;text-align:right;">
	<input type="checkbox" onclick="closeToday(<?=$no?>);" onkeypress="closeToday(<?=$no?>);" alt="닫기" style="height:20px;vertical-align:middle;line-height:20px;margin-right:4px">
	<label for="chk">오늘은 이창을 열지 않습니다.</label></div>
</div>

</form>
</body>
</html>
```
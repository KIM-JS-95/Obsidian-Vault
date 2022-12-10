# 스크롤링 이벤트 발생시키기

새로이 페이지를 리뉴얼하면서 기업의 연혁 / 수상 내역을 보여주는 페이지를 관리하게 되었다.

## 핵심

페이지의 상단에는 년도가 표시되며 년도를 클릭하면 해당 위치로 `SCROLLING`이동후 이벤트를 발생시킨다.

기본 구성은 `Anchor` 상태의 버튼과 `#` 링크로 구성하여 화면을 이동시킨 후 이벤트가 발생하도록 

`eventlitener` 를 추가시키도록 한다.

```html

<div id="tab">
    <a id="tab1" href="#1"></a>
    <a id="tab2" href="#2"></a>
    <a id="tab3" href="#3"></a>
</div>
<div id="history">
    <div id="1"></div>
    <div id="2"></div>
    <div id="3"></div>
</div>
```

페이지 스크롤링은 Client 가 해당 위치를 볼 수 있도록 이동하는 것이지만
**컴퓨터의 입장에서는 해당 위치를 보여주고있는지 모른다.**

컴퓨터가 이해할 수 있는 방법은 `전체 페이지의 크기`와 `디스플레이의 크기` 그리고 해당 `태그까지의 높이`를 이용하여 대략적인 높이 좌표를 확인하는 방법이다.

![](https://kingso.netlify.app/media/scrollHeight.jpg)

## 명령어

|            명령어            |           설명           |
|:-------------------------:|:----------------------:|
|   `$(window).height()`    | 디스플레이(window)가 보여주는 높이 |
|   `$(element).height()`   |         요소의 높이         |
|  `$(window).scrollTop()`  |       스크롤 위치(y)        |
| `$(element).offset().top` |     최상위부터 요소까지의 높이     |


스크롤 위치가
 
디스플레이의 의 높이 + 스크롤의 높이 (`$(window).height()` + `$(window).scrollTop()`) - A

스크롤의 높이 - 요소의 높이(`$(window).scrollTop()` - `$(elm).height()`) - B

가 범위 안에 존재하는지 검증한다.

> A > 스크롤 > B

## 코드

```js
// Jquery ver.

function checkVisible( elm, eval ) {
	eval = eval || "object visible";
	var viewportHeight = $(window).height(),
		scrolltop = $(window).scrollTop(),
		y = $(elm).offset().top,
		elementHeight = $(elm).height();   
	if (eval == "object visible") 
		return ((y < (viewportHeight + scrolltop)) && (y > (scrolltop - elementHeight)));
	if (eval == "above") 
		return ((y < (viewportHeight + scrolltop)));
}
    
 -- vanilla JS ver.
 
function checkVisible( elm, eval ) {
	 g=document.getElementsByTagName('body')[0],

	eval = eval || "object visible";
	var viewportHeight = g.clientHeight,
		scrolltop = document.scrollingElement.scrollTop,
		y = elm.getBoundingClientRect().top + window.pageYOffset,
		elementHeight = elm.clientHeight;
	if (eval == "object visible") 
		return ((y < (viewportHeight + scrolltop)) && (y > (scrolltop - elementHeight)));
	if (eval == "above") 
		return ((y < (viewportHeight + scrolltop)));
}
```

## 마무리

함수를 정의했다면 `window.addEventListener('scroll', function())`을 추가하여 스크롤 감지하도록 구성하고

감시하면 function 를 실행하도록 구성하면 된다.

```js
window.addEventListener('scroll', func);
var isVisible = false;
// 이벤트에 등록할 함수
const func = function () {
    if ( !isVisible && checkVisible('#1') ) {
        alert("엘리먼트 보임 !!");
        isVisible = true;
    }
    
    // 만일 리소스가 로드가 되면 더이상 이벤트 스크립트가 있을 필요가 없으니 삭제
    isVisible && window.removeEventListener('scroll', func);
}
```


# Reference

- [스크롤 인벤트 발생](https://inpa.tistory.com/entry/JS-%F0%9F%9A%80-%EC%8A%A4%ED%81%AC%EB%A1%A4-%EB%82%B4%EB%A0%A4%EC%84%9C-%ED%8A%B9%EC%A0%95-%EC%98%81%EC%97%AD-%EA%B0%90%EC%A7%80%ED%95%98%EA%B8%B0)
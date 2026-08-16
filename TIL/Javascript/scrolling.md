[[0-Javascript MOC.md]] · #javascript <!-- moc-nav -->

# 스크롤링 이벤트 발생시키기

새롭게 페이지를 리뉴얼하면서 기업의 연혁 / 수상 내역을 보여주는 페이지를 관리하게 되었다.

## 핵심

페이지의 상단에는 년도가 표시되며 년도를 클릭하면 해당 위치로 `SCROLLING`이동후 하리라이트 이벤트를 발생시킨다.

기본 구성은 `Anchor` 상태의 버튼과 `#` 링크로 구성하여 화면을 이동시킨 후 이벤트가 발생하도록 

`eventlitener` 를 추가시키도록 한다.

```html

<ul class="h_tab">
    <li class="on"><a href="#tab1">2020~</a></li><!--탭활성화 on-->
    <li class=""><a href="#tab2">2019~2010</a></li>
    <li class=""><a href="#tab3">2009~2001</a></li>
    <li class=""><a href="#tab4">2000~1993</a></li>
</ul>

<div class="sub_content">
    <!--2020~-->
    <div class="h_bx_w">
        <a name="tab1"></a>
        <div class="h_bx">
            <span class="year">2022</span>
            <span class="text"><span class="month">03.</span></span>
            <span class="text"><span class="month">06.</span></span>
        </div>
        <div class="h_bx">
            <span class="year">2021</span>
            <span class="text"><span class="month">03.</span></span>
        </div>
        <div class="h_bx">
            <span class="year">2020</span>
            <span class="text"><span class="month">06.</span></span>
            <span class="text"><span class="month">10.</span></span>
            <span class="text"><span class="month">11.</span></span>
        </div>
    </div>
    <!--//2020~-->
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
 
디스플레이의 의 높이 + 스크롤의 높이 (`$(window).height()` + `$(window).scrollTop()`) -> A

스크롤의 높이 - 요소의 높이(`$(window).scrollTop()` - `$(elm).height()`) -> B

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

### 🐋 TIMER 를 추가한 이유는 뭘까?

![](https://cdn.filestackcontent.com/Rxp5eCNUS2mACj9S2Pb0)

이벤트 스크롤은 윈도우에서 스크롤을 감지할 때마다 이벤트를 발생시키는데 이럴경우 한번 스크롤당 여러번의 function 이 발생하는데

이를 `디바운싱` 이라고한다. 

이를 피하기 위한 하나의 방법으로  타이머를 추가하여 간격을 두는 것이다.


```js
		const li = $('.h_tab li');
		var timer;

		function checkVisible( elm, eval ) {
			eval = eval || "object visible";
			var viewportHeight = $(window).height(),
				scrolltop = $(window).scrollTop(),
				y = $(elm).offset().top,
				elementHeight = $(elm)[0].parentElement.clientHeight;   
			if (eval == "object visible") 
				return ((y < (viewportHeight + scrolltop)) && (y > (scrolltop - elementHeight)));
			if (eval == "above") 
				return ((y < (viewportHeight + scrolltop)));
		}

		window.addEventListener('scroll', (event) => {
			if(timer) {
				clearTimeout(timer);
			}
			timer = setTimeout(function() {
				for(var i=1; i<=$('.h_tab li').length; i++){
					if(checkVisible($('[name="tab'+i+'"]'))){
						li[i-1].classList.add('on');
					}else{
						li[i-1].classList.remove('on');
					}
				}
			}, 100);
		},{passive: true});
```


# Reference

- [스크롤 인벤트 발생](https://inpa.tistory.com/entry/JS-%F0%9F%9A%80-%EC%8A%A4%ED%81%AC%EB%A1%A4-%EB%82%B4%EB%A0%A4%EC%84%9C-%ED%8A%B9%EC%A0%95-%EC%98%81%EC%97%AD-%EA%B0%90%EC%A7%80%ED%95%98%EA%B8%B0)
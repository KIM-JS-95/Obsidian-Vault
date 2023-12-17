# IFRAME 문서에서 js 일부기능이 먹히지않는 현상


>iframe이란 inline frame의 약자입니다.
>
>iframe 요소를 이용하면 해당 웹 페이지 안에 어떠한 제한 없이 또 다른 하나의 웹 페이지를 삽입할 수 있습니다.

우리 모두 이렇게 이해하고 있겠지만 삽입된 문서에서 기능을 구현해야한다면 이야기는 달라진다.

## 뭐가 문제인데?

다음과 같은 파일이 있다고 가정하자.

```html

// A document
<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <title id="title">HTML Iframes</title>
</head>

<body>
<h2>iframe태그를 이용한 웹 페이지 삽입 1</h2>

// B document
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>HTML Iframes</title>
</head>
<body>
<h2>iframe태그를 이용한 웹 페이지 삽입 1</h2>

<script>
            // A 문서의 제목을 빨간색으로 변경합니다.
            $("#title").css('style','red');
        </script>
</body>
</html>

</body>
</html>

```

A 문서 내부에 B 문서를 `inline` 했기때문에 <u>B 문서가 A에 포함</u>되어있다고 이해는것이 틀리진 않지만 

함수를 사용할 경우 접근 방식을 달리해야한다.

## B 문서에서 A 문서의 TITLE 태그의 색깔을 변경하는 JS를 입력한다면 기능은 작동을 할까?


결과적으로 B 문서의 `function`은 A 문서를 컨트롤 할 수 없다. (다시말해, 접근할 수없다.)

웹에서 본다면 하나의 코드 문서로 보여지겠지만 이 둘은 엄연히 다른 문서로 존재하기때문에 `inline`이라는 의미가 맞는지 생각하게된다.

나는 이런 문제를 `삽입하다(insert)` 보다는 **문서위에 문서는 올려둔다** 라는 의미가 적합하다 생각한다.

그러지 않고서야 `$(window.parent)` 함수가 필요한 이유가 없다.

## `$(window.parent)` ??

`$(window)` 함수는 현재 위치의 문서를 접근하는 함수이며 `parent` 를 추가한다면 <u>해당 문서의 부모 문서를 바라본다는 의미이다.</u>

> 즉, 예시 코드는 하나의 코드가 아닌 부모와 자식 관계의 문서 형태를 가진다는 의미이다.

위 예시를 수정한다면 `$(window)` 를 `$(window.parent)` 으로 고쳐야한다.

```html

// A document
<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <title id="title">HTML Iframes</title>
</head>

<body>
<h2>iframe태그를 이용한 웹 페이지 삽입 1</h2>
 
// B document
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>HTML Iframes</title>
    </head>
    <body>
    <h2>iframe태그를 이용한 웹 페이지 삽입 1</h2>
    
        <script>
            // A 문서의 제목을 빨간색으로 변경합니다.
            $(window.parent).$("#title").css('style','red');
        </script>
    </body>
    </html>

</body>
</html>

```

## 정리

iframe 으로 삽입한 문서의 관계에 대해 다시 생각해본다면 많은 기능을 수정할 수 있을것이다.

삽입이 아닌 올려둔다 라는 의미로 그리고 두 문서가 부모와 자식 관계를 가진다는 것으로 생각해보는 건 어떨까?



# Reference
- [iframe](https://www.tcpschool.com/html/html_space_framesIframes)
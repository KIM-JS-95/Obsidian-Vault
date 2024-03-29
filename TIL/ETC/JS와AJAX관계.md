
## 지금 까지의 비동기 통신

지난 시간 대략 3가지의 포트폴리오 제작을 하면서 `FE`에서 `BE`로 데이터를 전송하기 위해 **Jquery 방식의 `Ajax`를 많이 사용해왔다.**

```bash
$('#save').on('click', function () {
    var data={
             title: $('#title').val(),
             content: $('#content').val(),
             link: $('#link').val()
         };

     $.ajax({
         type: 'POST',
         url: '/gallary/create',
         contentType:'application/json; charset=utf-8',
         data: JSON.stringify(data)
     }).done(function(){
      alert('저장 성공');
      window.location.href='/home/guest'
     }).fail(function (error) {
     alert(JSON.stringify(error));
     });
 });
```

### 나의 지나온 개발환경

백엔드 개발 방향으로 성장해 오면서 포트폴리오를 완성하기 위해 어느 수준의 웹과 서버의 통신을 이해해야했다.
그러나 JS와 JAVA 그리고 Spring 이라는 언어를 **짧을 기간에 이해하고 통신을 구현하는 과정은 독학으로서 혹은 관련 경험의 부족하다면 힘든 과정일 것이다.**

때문에 많은 국비학원에서는 `제이쿼리`로 Ajax를 구현하는 과정을 교육하고 있다.

**그러나 실무 환경의 제이쿼리는 2022년 개발 트렌드를 쫒아올 수 있을까?**

### 자바스크립트의 미쳐버린 성장

더욱 오래전에는 `JSP(자바 서블릿 페이지)` 혹은 `XML`을 이용해오면서 JAVA 한가지로 웹개발을 할수가 있었지만 크롬, 사바리의 등장으로
웹 어플리케이션 환경에서의 호환성 문제가 나타나기 시작했다.

그리하여 탄생한 언어가 스크립트 기반의 `JS`인것이다.

초기 JS는 웹 개발 환경에서 자바에서 밀렸지만 2010년 이후 혹은 이전부터 `뷰`, `리액트`, `노드` 등의 프레임워크 혹은 라이브러리가 등장하면서
JS의 입지가 넓혀지고 있으며 현재는 백엔드 영역까지 기능을 확장하고 있다.

### 각광 받은 라떼는 제이쿼리

![](http://wiki.hash.kr/images/e/ed/%EC%A0%9C%EC%9D%B4%EC%BF%BC%EB%A6%AC_%EA%B8%80%EC%9E%90.png)

제이쿼리는 2006년 AJAX를 목적으로 만들어진 `JS라이브러리`이다.
이미 10년 이상 각광 받은 라이브러리 이지만 여기에는 단점이있다.
- 디버깅, 에러 핸들링이 어려움
- 코드 관리
- 업데이트 및 관리
- `가상DOM`과 상성이 좋지 못함

그러나 근본적인 원인은 언어의 발전에 따라가지 못하였다고 생각한다.


### 강력해진 JS 라이브러리

지금까지도 `자바스크립트`는 진화하고있다.

그 말은 순수 자바스크립트를 알고있다면 AJAX를 구현할 또 다른 방법을 찾을 수 있을 것이다.

**2015년 `자바스크립트 ES6`가 등장하면서 `fetch API`가 새로운 통신 방법으로 등장했다.**
이전 방식보다 더욱 간단한 방법으로 AJAX 통신이 가능하게 되면서 프로트엔드와 백엔드의 구분이 더욱 명확해진 계기가 나타난 것이다.

또한 `순수 JS`이기 때문에 **AJAX뿐만 아니라 여러 프레임워크 혹은 라이브러리와 호환이 가능하게 되어** 
많은 것들을 JS로만 구현할 수 있게 된것이다.


## fetch 와 AJAX

현재는 많은 백엔드 강의는 주로 `제이쿼리` 방식의 AJAX를 교육하고 있지만 전문적 JS강좌에서는 `fetch메소드`를 알려주고 있다.




## fetch CRUD 메소드

### GET

→ 단순히 원격 API에 있는 데이터를 가져올 때 쓰임

→ fetch함수는 디폴트로 GET 방식으로 작동하고, 옵션 인자가 필요 없음.

→ 응답(response) 객체는 json() 메서드를 제공하고, 이 메서드를 호출하면 응답(response) 객체로부터 JSON 형태의 데이터를 자바스크립트 객체로 변환하여 얻을 수 있음.

```
fetch("https://jsonplaceholder.typicode.com/posts/1") // posts의 id 1인 엘리먼트를 가져옴
    .then((response) => response.json())
    .then((data) => console.log(data))
```

### POST

→ 폼 등을 사용해서 데이터를 만들어 낼 때, 보내는 데이터의 양이 많거나, 비밀번호 등 개인정보를 보낼 때 POST 메서드 사용

→ 새로운 포스트 생성 위해서는 method 옵션을 POST로 지정해주고, headers 옵션으로 JSON 포맷 사용한다고 알려줘야 함. body 옵션에는 요청 데이터를 JSON 포맷으로 넣어줌.

method – HTTP 메서드

headers – 요청 헤드가 담긴 객체(제약 사항이 있음)

body – 보내려는 데이터(요청 본문)로 string이나 FormData, BufferSource, Blob, UrlSearchParams 객체 형태

```html
fetch("https://jsonplaceholder.typicode.com/posts", {
    method: "POST", // POST
    headers: { // 헤더 조작
     "Content-Type": "application/json",
    },
    
    body: JSON.stringify({ // 자바스크립트 객체를 json화 한다.
        title: "Test",
        body: "I am testing!",
        userId: 1,
    }),
})
    .then((response) => response.json())
    .then((data) => console.log(data))
```

### PUT (전체 수정)

PUT: 존재하는 자원 변경 요청

→ API에서 관리하는 데이터의 수정을 위해 PUT 메서드 사용함.

→ method 옵션만 PUT으로 설정한다는 점 빼놓고는 POST 방식과 비슷

→ 아예 전체를 body의 데이터로 교체해버림.

```html
fetch("https://jsonplaceholder.typicode.com/posts", {
    method: "PUT",
    headers: {
        "Content-Type": "application/json",
        },
    body: JSON.stringify({
    title: "Test" // 아예 title 엘리먼트로 전체 데이터를 바꿈. 마치 innerHTML같이.
    }),
})
    .then((response) => response.json())
    .then((data) => console.log(data))
```

### Patch (부분 수정)

PATCH: 존재하는 자원 일부 변경 요청

→ body의 데이터와 알맞는 일부만을 교체함 .

```
fetch("https://jsonplaceholder.typicode.com/posts/1", { // posts의 id 1인 엘리먼트를 수정
    method: "PATCH",
    headers: {
        "Content-Type": "application/json",
},
    body: JSON.stringify({
        title: "Test" // title만 바꿈. 나머지 요소는 건들지 않음.
    }),
})
    .then((response) => response.json())
    .then((data) => console.log(data))
```

### fetch API - DELETE Method

DELETE: 존재하는 자원 삭제 요청

→ 보낼 데이터가 없기 때문에 headers, body 옵션이 필요없음

```html
fetch("https://jsonplaceholder.typicode.com/posts/1", {
    method: "DELETE",
    })
        .then((response) => response.json())
        .then((data) => console.log(data))
```

## 정리

이제는 `제이쿼리`와 `타임리프`를 버리고 순수JS를 사용하여 통신을 공부해야할 때가 왔다.
분명 개발 초기에는 직관적인 제이쿼리를 공부하는 것도 좋은 방안이지만 어느 정도의 개발 능력에 도달했다면 
**JS를 공부하는 것도 어쩌면 좋은 방향일거라고 생각한다.**



## Reference
- [Ajax, fetch](https://velog.io/@ksh4820/Ajax-fetch)
- [AJAX 서버 요청 및 응답 fetch api 방식](https://inpa.tistory.com/entry/JS-%F0%9F%93%9A-AJAX-%EC%84%9C%EB%B2%84-%EC%9A%94%EC%B2%AD-%EB%B0%8F-%EC%9D%91%EB%8B%B5-fetch-api-%EB%B0%A9%EC%8B%9D)
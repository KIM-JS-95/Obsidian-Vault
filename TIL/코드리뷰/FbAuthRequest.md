# 페이스북 login API에서의 권한추가

## 목차

> 1. [[#개요]]
> 2. [[#앱 권한 강화 방법]]
> 3. [[#API]]
> 4. [[#Reference]]

# 개요
페이스북 login api에서 유저를 호출하면 기본으로 제공되는 정보가 있는데

`public_profile`,`email` 이다.

혹여 사용자 정보를 저장함에 따라 추가적인 정보를 획득하고 싶다면 권한을 추가 요청을해야한다.

![](/image/auth_function.png)

페이스북에서는 앱권한 요소를 2가지 Advenced 와 Standard 로 구분한다.

앞서 말한 `public_profile`,`email` 가 Advenced에 해당하는 요소이며 관리자가 해당사용자의 추가적인 정보를 가져오고 싶다면
그 외의 요소를(Standard)에서 Advenced로 업그레이드를 해야한다.

# 앱 권한 강화 방법

페이스북에서 제시한 앱 권한 변경을 요청하는 방법은[API](https://developers.facebook.com/tools/explorer)을 통해서 필요한 요소의 
테스트를 진행후 앱권한 페이지로 돌아와 `앱 겁수 요청` 버튼을 클릭하면 끝이다.

페이스북에서 이를 확인하고 권한을 추가하는것은 대략 10일이 걸린다.

# API
권한 등록이 완료 되었다면 해당 코드를 적용해야한다.

```js
FB.login(function(response) {
	if (response.status === 'connected') {
		FB.api('/me', 'get', {fields: 'name,email, gender, hometown'}, 
			function(r) {
			console.log(r);
			})
	} else if (response.status === 'not_authorized') {
		alert('앱에 로그인해야 이용가능한 기능입니다.');
	} else {
		alert('페이스북에 로그인해야 이용가능한 기능입니다.');
	}
}, {scope: 'public_profile,email, gender, hometown'});
```

위 코드에서 `fields`와 `scope`에 요소를 추가해줘야 정상 작동된다.


# Reference
- [facebook app auth](https://developers.facebook.com/docs/marketing-api/overview/authorization?locale=ko_KR)


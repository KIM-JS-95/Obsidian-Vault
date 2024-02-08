
# 날짜: 2024-02-07 ~ 2024-02-26

## 목차

> 1. [문제 발생 위치]
> 2. [문제 현상] 
> 3. [디버깅 과정]
> 4. [결과]
> 5. [기타 메모]
> 6. [참조 영역]


## 문제 발생 위치
- 페이스북 소셜 로그인 정책 변경에 따른 기존 자사 로그인 서비스 수정
## 문제 현상
자사의 회원가입 프로세스에 대해 페이스북으로 부터 정책 확인과 회원가입 절차 수정 통보가 접수 되었다.

요구사항은 **페이스북 유저로 가입을 원하는 유저는 추가 정보를 요구하기 않을 것** 인데
사실 확인을 위해 소셜 로그인 API 페이스북 정책 및 약관을 찾아봐도 이와 관련한 약관은 찾아볼 수 없었다.

그래도 페이스북 요청을 이행하지 못한다면 소셜로그인 뿐만 아닌 자사와 관련한 모든 서비스가 중단된다하니 수정을 할 수 밖에 없다.


우선 자사 회원가입 절차는 3단계로 구성되어 있고, FB에서 시정을 요구한 단계가 3단계 과정이다.
```

1. 대상 SNS에서 유저의 이름과 이메일을 획득
2. 자사 회원가입 정책 및 이용약관 동의 확인
3. 추가 정보(성별/ 생일/ 지역 / 전화번호)를 작성

```
## 디버깅 과정
1. 회원가입을 위한 필요한 데이터 확인

소셜 회원가입 과정에서 자사가 요구하는 회원 정보는 다음과 같다.
```

이메일(아이디), 주소, 생일, 전화번호

```
페이스북 요구대로 **3단계 과정**을 제외한다는 것은 제외되는 <u>성별 / 주소 / 생일 / 전화번호</u> 정보를 
다른 방식으로 받아야 한다는 것인데 가장 빠른 방법은 페이스북 API로 받는 방법이였다.

또 다른 문제라면 위 3가지 요소는 facebook에서 필수 입력정보가 아니기 때문에 데이터가 누락 되어있을 경우 
자사입장에서는 회원가입이 불가능 할 수 밖에 없다는 것이다.

하지만 자사에서 별도로 사용하지 않던 데이터이기 때문에 전략팀 요청에 따라 `필수 데이터`에서 `선택 데이터`로 전환을 결정했고 테이블을 수정하는 것으로 회원가입 방식을 변경 하기로 했다.

2. Facebook App 권한 추가 및 앱 검수 요청

FACEBOOK APP 생성을 완료했다면 기본으로 설정되어 있는 권한(Advanced access)은 `Email / Public_scope` 두 가지이다.
그러나 경우에 따라 추가 정보가 필요하다면 Graph API 테스트를 통해 Standard access에서 Advance access로 전환 요청을 제시할 수 있다.

![](/image/FBAccess.png)

자사의 경우에 `성별 ~ 전화번호` 데이터가 필요했기에 API테스트를 진행하여권한을 추가 요청할 수 있었다. 
(요청에 대한 검수는 대략 10일 이내이다.)

[페이스북API_권한_요청](./FbAuthRequest.md)

3. 데이터 획득의 형평성과 로직 수정
이번 문제의 중심은 유저에게 별도의 추가 데이터를 요청 단계를 페이스북 로그인 유저에 대해서만 제외하는 것이지만
자사는 페이스북 뿐만 아닌 구글 / 카카오톡 / 네이버 / 애플에서도 소셜 로그인 기능을 이용하고 있기에
페이스북 유저의 추가 정보 획득을 제한하는 것은 다른 이용자와의 형평성에 위반하는 것이다. 

전략팀은 이후 24년 03월 부터 유저에 대한 추가 정보 획득 단계 즉 3단계를 모두 제외하기로 했으며
결과적으로 내가 할일은 3단계해 해당하는 모든 변수를 제회하고 API를 재검토하는 것이다.
 
## 결과

## 기타 메모

1. 유저 전화번호 정보는 API를 통해 획득할 수 없다.
페이스북은 유저의 개인정보 보호정책으로 전화번호는 요청할 수 없다.
GraphAPI를 통해 유저의 추가 데이터를 얻고자 한다면 페이스북에서 제공하는 정보 범위를 확인하여 개발을 진행하도록 하자.

2. Email 획득 버그
API 사용을 위한 앱 권한이 적용되어있고 코드 내부에 권한(SCOPE)가 정상적으로 입력이 되어있음에도
이메일 데이터를 받을 수 없다면 다음 문제를 확인하고 해당되는 것이 있다면 Email 버그일 가능성이 있으니 다른 사용자로 로그인을 테스트 해보자

> 1. 최초가입시 이메일을 입력하지 않은경우
> 2. 회원가입 후 이메일을 별도로 추가 입력한 경우
> 3. 형식에 맞지 않는 이메일 주소를 사용한 경우


> * 타사의 FACEBOOK LOGIN은 어떻게 되어있을까?
>
> - SBS : 이메일정보 누락시 가입 불가 "SNS Token Error" 경고창 노출
> - KBS : 이메일 정보 필요하지 않음 -> SNS 로그인은 회원정보 수정 불가
> - MBC : 이메일 정보 누락시 가입 불가 -> 다른 방식으로 우회
> - 한국일보 : 이메일 정보 필요하지 않음 -> 필명(닉네임) 입력 방식으로 계정ID를 대체 / 뉴스레터 가입 불가
> - 중앙일보 : 가입 실패 -> 다른 방식으로 우회

해당 문제는 최소 4년전부터 지속적으로 발생하던 문제이며 현재까지도 해결되지 않는 문제이다.
때문에 이메일을 습득  버그가 발생했다면 다른 방법을 고민해 봐야한다.

## 참조 영역
- [이메일 버그: facebook developer community center](https://developers.facebook.com/community/threads/217771886049828/)

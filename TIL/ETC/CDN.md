## CDN -  콘텐츠 전송 네트워크

### CDN의 목적
`CDN`은 사용자가 웹에서 콘텐츠 사용의 효율성 향상을 목적으로 두는 네트워크로
특히 인터넷으로 용량이 큰 콘텐츠 전송에 따른 트래픽 폭주현상으로 인한 네트워크 혼잡
문제를 해결하기 위해 개발된 네크워크 이다.


### 작동원리

1. 최초 요청은 서버로 부터 컨텐츠를 가져와 고객에게 전송하며 동시에 `CDN 캐싱장비`에 저장한다.
2. 두번째 이후 모든 요청은 CDN 업체에서 지정하는 해당 컨텐츠 만료 시점까지 `CDN 캐싱장비`에 저장된 컨텐츠를 전송한다.
3. 자주사용하는 페이지에 한해서 `CDN 장비`에서 캐싱이 되며, **해당 컨텐츠 호출이 없을 경우 주기적으로 삭제된다.**
4. 서버가 파일을 찾는 데 실패하는 경우 **CDN 플랫폼의 다른 서버에서 콘텐츠를 찾아 엔드유저에게 응답**을 전송한다.
5. 콘텐츠를 사용할 수 없거나 콘텐츠가 오래된 경우, 
CDN 은 서버에 대한 요청을 프록시로 작동하여 향후 요청에 대해 응답할 수 있도록 새로운 콘텐츠를 저장한다.


### CDN 캐싱?

동일 유저가 동일 데이터를 호출하느 경우 기존데 기록된 즉 캐싱된 데이터를 가져오는 것이 현명하다.

이러한 캐신 방식에는 2가지가 존재한다.

1. Static Caching

   - Origin Server에 있는 Content를 운영자가 미리 **Cache Server에 복사**
   - 미리 복사해 두기 때문에 사용자가 Cache Server에 Content를 요청시 무조건 Cache Server에 있다.
   - 대부분의 국내 CDN에서 이 방식을 사용( ex. NCSOFT 게임파일 다운로드 등)


2. Dynamic Caching

- Origin Server에 있는 Content를 운영자가 미리 **Cache Server에 복사하지 않음**
- 사용자가 Content를 요청시 해당 Content가 없는 경우 Origin Server로 부터 다운로드 받아 전달한다.
  - (Content가 있는 경우는 캐싱된 Content 사용자에게 전달.)
- 각각의 Content는 일정 시간이후 Cache Server에서 삭제될 수도 있다. (계속 가지고 있을 수도 있음)
 

### CDN이 가진 기술

1. Load Balance
- 사용자에게 콘텐츠 전송 요청(Delivery Request)을 받았을 때, 최적의 네트워크 환경을 찾아 연결하는 기술, 
  - GSLB(Global Server Load Balancing)이라고도 한다.
- 물리적으로 가장 가깝거나 여유 트래픽이 남아 있는 곳으로 접속을 유도하는 기술이다.


2. Contents Deploy


3. traffic detection

## Reference
- [갓대희의 작은공간:티스토리](https://goddaehee.tistory.com/173)
- [CDN(콘텐츠 전송 네트워크)이란 무엇인가요?](https://www.akamai.com/ko/our-thinking/cdn/what-is-a-cdn)
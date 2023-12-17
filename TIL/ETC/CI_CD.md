# CI와 CD는 뭘까?

## CI(Continuous Integration)

코드 버전 관리를 하는 VCS 시스템에 PUSH가 되면 자동으로 Test, Build가 수행되고 

Build 결과를 운영 서버에 배포까지 자동으로 진행되는 이 과정을 CI (지속적 통합)이라고 합니다.

> VCS 시스템?
> 
> 버전 관리 시스템(Version Control System)
> 
> 동일한 정보에 대한 여려 버전을 관리하는 것을 말한다.
> 
> 코드 변화의 기능 개선과 버그 수정, 요구사항에 따른 프로그래밍 소스 수정을 관리하는 시스템을 말하며
> 
> 변경점을 저장하여 기록의 열람, 복원 기능과 변경 사항을 함께 저장하며 충돌을 방지한다.

### CI의 4가지 규칙 
- 모든 소스 코드가 살아있고(현재 실행되고) 어느 누구든 현재의 소스를 접근할 수 있는 단일 지점을 유지할 것
- 빌드 프로세스를 자동화시켜서 어느 누구든 소스로부터 시스템을 빌드하는 단일 명령어를 사용할 수 있게 할 것
- 테스팅을 자동화시켜서 단일 명령어를 통해서 언제든지 시스템에 대한 건전한 테스트 수트를 실핼할 수 있게 할 것
- 누구나 현재 실행 파일을 얻으면 지금까지 최고의 실행파일을 얻었다는 확신을 하게 만들 것



# Reference
- [CI?](https://jojoldu.tistory.com/265)
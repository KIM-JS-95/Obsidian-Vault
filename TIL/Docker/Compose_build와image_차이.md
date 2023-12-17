# 🐋 컴포넌트에서의 build 와 image의 차이 🐋

## 🍃 image

`image` means docker compose will run a container based on that image

Docker Hub에서 해당 이미지를 다운로드 후 이미지에서 컨테이너를 실행한다.

## 🍃 build

`build` means docker compose will first build an image based on the Dockerfile found 
in the path associated with build (and then run a container based on that image).

해당 경로의 `Dockerfile`을 기반으로 먼저 이미지를 빌드하고 그것을 기반으로 컨테이너를 실행한다.



## 🍃 궁금증 발생

### 1.`build` 명령어 보다 `image`를 사용하는 것이 좋지 않을까?

[StackOverFlow](https://stackoverflow.com/questions/42170124/docker-compose-when-to-use-image-over-build) 에 따르면 `build` 명령어를 2가지 상황에서 사용하기를 권장했다.

- development
- automated testing

일반적으로 `build`는 image를 코드 프로덕션이 준비 중이거나 테스트 과정에서 사용함을 알렸으며 이후 개인 Docker Hub에 이미지를 업로드 하여
불러오는 방식으로 설계한다 말한다.

다시말하면 Hub에 존재하는 image는 이미 검증된 이미지 이며 사용하기 안전함을 주장했고 

`build` 대상이 되는 Dockerfile의 경우 빠른 테스트를 확인할 수 있는 장점과 Hub의 반복적인 push를 피하기 위함인 것이다.

### 2. 정리

그러나 `@GHETTO.CHILD` 유저의 코멘트에는 **항상 이러한 방법이 해답은 아니다.** 라고 알렸다. 

즉, 작업의 흐름에 따라 변경될 수 있는 문제이며 이것은 회사의 지침을 따르는 것이 좋다 말한다.

- How teams run their build, ship, deploy varies greatly as they figure out what works best for them and their product so the above build . scenarios may not be accurate for all cases, but is accurate for how my company uses compose.
- This assumes build . in a docker-compose context and not a docker
 build context.

# 🐋 Reference

- [Docker Compose when to use image over build - StackOverFlow](https://stackoverflow.com/questions/42170124/docker-compose-when-to-use-image-over-build)
- [Difference between 'image' and 'build' within docker compose - StackOverFlow](https://stackoverflow.com/questions/34316047/difference-between-image-and-build-within-docker-compose)
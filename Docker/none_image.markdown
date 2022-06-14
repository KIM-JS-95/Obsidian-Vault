# 이미시 build 시 생성되는 <none> image

Docker 개발시 자주 볼 수 있는 이미티 형태로 개발자의 코드가 잘못된 것이 아닌 Docker 자체의 부산물이다.

## 🦐 Docker 이미지 파일 시스템과 이미지 계층의 구성 방식
각각의 도커 이미지는 레이어로 구성되며 이러한 레이어는 서로 `부모-자식 계층관계`를 가진다.

이러한 이미지는 `/var/lib/docker/graph` 에 저장되고 때문에 도커에서는 `graph database`라고 말한다.

작업한 Dockerfile을 `pull`, `build` 시 동일 이미지 Name이 존재할 경우 이미지 중복을 피하기 위해 기존의 이미지와 태그를 <none>으로 변경하고
자식 계층으로 새로운 이미지를 빌드 하게 되는 것이다.

Docker 에서는 이렇게 버려진 이미지를 `dangling image`라고 부른다.


![](https://projectatomic.io/images/parent-child.png?1633620578)

## 🦐 dangling image 관리

Java는 GC 시스템을 통해 더 이상 참조하지 않는 변수를 관리하는 시스템을 가지고 있어 메모리 관리에서 우수함을 보인다.

더 이상 참조하지 않는 변수의 개념은 Docker에서도 존재하는데 `dangling image`이미지가 바로 그것이다.

오랜기간 `dangling image`를 관리하지 않는 다면 **디스크 공간 문제의 원인**이 되기 때문에 사용자는 지속적으로 이미지를 관리 해주어야한다.


## 🦐 none images 삭제

```shell
 docker rmi $(docker images -f "dangling=true" -q)
 
 or 
 docker image prune
```


# Reference
- [[Docker] <none> image야 잘 가~!](https://elsboo.tistory.com/3)
- [What are Docker <none>:<none> images?](https://projectatomic.io/blog/2015/07/what-are-docker-none-none-images/)
- [Why the "none" image appears in Docker and how can we avoid it - StackOverFlow](https://stackoverflow.com/questions/53221412/why-the-none-image-appears-in-docker-and-how-can-we-avoid-it)

# 🐋 Volume and Mount 🐋

`Volume` 및 `bind Mount` 를 사용하면 호스트 시스템과 컨테이너 간에 파일을 공유할 수 있으므로 컨테이너가 중지된 후에도 데이터를 유지할 수 있다.


## 🦐 Volume

> Volume 은 Docker 컨테이너에서 생성하고 사용하는 데이터를 유지하기 위한 기본 메커니즘이다.

`Volume`이 Docker에 의해 관리되고 호스트 시스템의 핵심 기능에서 분리된다는 점을 제외하고는 `바인딩 마운트`가 작동하는 방식과 유사하다.

다만 `바인드 마운트`는 **호스트 시스템의 디렉토리 구조 및 OS 에 따라** 다르지만 `볼륨`은 Docker에서 완전히 관리된다.

### 장점

- 볼륨은 바인드 마운트보다 백업 또는 마이그레이션이 더 쉽다.
- Docker CLI 명령 또는 Docker API를 사용하여 볼륨을 관리할 수 있다.
- 볼륨은 Linux 및 Windows 컨테이너 모두에서 작동한다.
- 여러 컨테이너 간에 볼륨을 더 안전하게 공유할 수 있다.
- 볼륨 드라이버를 사용하면 원격 호스트 또는 클라우드 공급자에 볼륨을 저장하고 볼륨의 내용을 암호화하거나 다른 기능을 추가할 수 있다.
- 새 볼륨의 콘텐츠는 컨테이너에 의해 미리 채워질 수 있다.
- Docker Desktop의 볼륨은 Mac 및 Windows 호스트의 바인드 마운트보다 성능이 훨씬 높다..


볼륨을 사용하는 컨테이너의 크기(용량)를 늘리지 않고
볼륨의 콘텐츠가 지정된 컨테이너의 수명 주기 외부에 있기 때문에
컨테이너의 쓰기 가능 계층에 데이터를 유지하는 장점이 있다.

![](https://docs.docker.com/storage/images/types-of-mounts-volume.png)

## 🦐 Bind Mount
바인드 마운트를 사용하면 호스트 시스템 의 파일 또는 디렉토리가 절대 경로로 컨테이너에 마운트되며`Volume`에 비해 굉장히 제한적이다.

우수한 성능을 가지고 있지만 특정 디렉토리 구조를 사용할 수 있는 호스트 시스템의 파일 시스템에 의존한다.

![](https://docs.docker.com/storage/images/types-of-mounts-bind.png)


## 🦐 tmpfs 마운트

Linux에서 Docker를 실행하는 경우 세 번째 옵션인 `tmpfs 마운트`가 있다. 

마운트 를 사용하여 컨테이너를 생성할 때 `tmpfs컨테이너`는 컨테이너의 쓰기 가능 계층 외부에 파일을 생성할 수 있다.

볼륨 및 바인드 마운트와 달리 `tmpfs마운트`는 `호스트 메모리`에서 임시적으로 저장되며
컨테이너가 중지되면 `tmpfs마운트`가 제거되고 거기에 기록된 파일은 유지되지 않는다.

**정리하면, 볼륨 및 바인딩 마운트와 달리 tmpfs컨테이너 간에 마운트를 공유할 수 없으며
Linux에서 Docker를 실행하는 경우에만 사용할 수 있습니다.**

![](https://docs.docker.com/storage/images/types-of-mounts-tmpfs.png)



# 🐋 Reference
- [docker data volume vs mounted host directory - StackOverFlow](https://stackoverflow.com/questions/34357252/docker-data-volume-vs-mounted-host-directory)
- [docker docs](https://docs.docker.com/storage/bind-mounts/)
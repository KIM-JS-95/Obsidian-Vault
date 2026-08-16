[[0-Docker MOC.md]] · #docker <!-- moc-nav -->

# 🐋 Dockerfile build error 🐋


Dockerfile로 `./gradlew build` 할 경우 

> Error with gradlew: /usr/bin/env: bash: No such file or directory


에러가 발생한다. Dos환경과 unix 환경의 차이에서 나타나는 현상같으니
바꿔주면된다.

```
sudo apt-get install dos2unix
dos2unix ./gradlew
./gradlew bootRun
```
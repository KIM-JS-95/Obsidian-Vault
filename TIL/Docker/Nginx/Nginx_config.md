
# nginx.conf 와 default.conf 의 차이점

## nginx.conf
```shell
vi /etc/nginx/nginx.conf
vim /etc/nginx/nginx.conf
nano /etc/nginx/nginx.conf

user  nginx;
worker_processes  1;
error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;         //Process가 동시에 처리 가능한 접속자 수 
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;      // 웹서버의 기본 Content-Type을 정의한다.
    
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
    access_log  /var/log/nginx/access.log  main;
    sendfile        on;
    #tcp_nopush     on;
    keepalive_timeout  65;
    #gzip  on;
    include /etc/nginx/conf.d/*.conf        // ** 핵심 ** 
}
```

## default.conf
```shell
vi /etc/nginx/conf.d/default.conf
vim /etc/nginx/conf.d/default.conf
nano /etc/nginx/conf.d/default.conf
# nginx 설치 후, default.conf 파일을 연다.

server {
    listen       80;
    server_name  localhost;
    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}
```

`nginx.conf` 파일 내부를 보면 default.conf 가 include 되어있다.

즉, default.conf는 nginx.conf를 통해 include된 서버 설정관련 파일이며 
default2.conf, default3.conf 등 여러 개의 파일을 추가하여 서버관련 설정을 추가로 만들어 포함시킬 수 있다.

# 결론
많은 이와 관련한 포스팅을 본다면 다른 파일에서 작업하는 개발자들을 볼 수 있는데 사실 어느 방식을 사용해도 문제가 없으며
관리하기 쉬운 방향으로 개발하면 될것이다.

`nginx.conf` 파일은 Nginx의 핵심 파일이며 `default.conf`는 개발자의 목적에 따라 커스텀이 가능한 파일이기
때문에 **default** 라는 파일명을 유지할 필요는 없으며 `http{}` 내부에 include 해주기만 하면 된다.

# Reference
- [Nginx 설치 및 nginx.conf, default.conf 이해하기](https://phsun102.tistory.com/45)
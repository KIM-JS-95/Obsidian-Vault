# LDAP (Lightweight Directory Access Protocol)

LDAP는 디렉터리 서비스에 접근하기 위한 X.500의 경량 확장된 프로토콜로
디렉터리 서비스는 네트워크 상의 사용자, 컴퓨터, 프린터 등의 자원을 조직화하고 관리하는 데 사용된다.

LDAP는 TCP/IP를 통해 디렉터리 서비스에 액세스할 권한을 제공하는 것으로 접근할 수 있다.

## 주요 특징
- **경량 프로토콜**: LDAP는 X.500 디렉터리 접근 프로토콜(DAP)에 비해 경량화된 프로토콜
- **트리 구조**: 디렉터리 정보는 트리 구조로 조직화됩니다.
- **표준화**: LDAP는 IETF의 표준 프로토콜입니다.

```
💡 X.500 이란?
디렉터리 서비스에 대한 국제 표준으로 네트워크에서 리소스와 사용자 정보를 조직하고 관리하는 데 사용된다. 

X.500는 이러한 디렉터리 서비스를 정의하고 구현하기 위한 일련의 프로토콜과 모델을 제공한다.
```


## 차이점

- LDAP은 OSI 네트워크를 기반한 X.500과 달리 TCP/IP 네트워크를 기반으로 구성되어 더욱 경량화된 구성이 가능하다.

- LDAP 서버에 저장되는 데이터 구조는 X.500과 마찬가지로 **TREE 형태의, Object와 Attribute로 구성된다.** 다만, Object 식별자 **DN(Distringuish Name)**는 숫자 타입이 아닌 문자열 타입이다.

- LDAP의 서버는 독립적이고 오직 클라이언트와 통신한다. 즉, X.500의 DSP(Directory System Protocol)가 없고, 클라이언트가 요청하는 정보가 서버에 존재하지 않으면 해당 정보가 저장된 다른 서버에 대한 URL로 응답한다. 이로 인해, LDAP은 요청에 대한 범위가 한정됩니다.

- X.509 프로토콜로 보안 구성을 하는 X.500과 달리 SASL(Simple Authentication and Security Layer)로 보안 구성이 가능하여 더욱 유연한 보안 구성이 가능하다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fcubye8%2FbtqB0gmHtKN%2F91XK4hN9J9Y5pKDJSPvTy0%2Fimg.png)

## 사용 사례
- **인증 및 권한 부여**: LDAP는 사용자 인증 및 권한 부여에 널리 사용
- **주소록 서비스**: 이메일 클라이언트에서 주소록 서비스를 제공하는 데 사용
- **네트워크 자원 관리**: 네트워크 상의 다양한 자원을 중앙에서 관리하는 데 사용

## 기본 용어
- **DN (Distinguished Name)**: 디렉터리 내의 항목을 고유하게 식별하는 이름이다.
- **RDN (Relative Distinguished Name)**: DN을 구성하는 각 부분
- **Entry**: 디렉터리 내의 하나의 객체
- **Attribute**: Entry의 속성을 나타낸다.

- **dc (Domain Component)**: 도메인을 나타내기 위한 속성이며
    도메인 `www.mydomain.com`은 `DC=www,DC=mydomain,DC=com`으로 표현할 수 있습니다.

- **ou (Organization Unit)**: 그룹, 조직을 나타내기 위한 속성이다. 
    예를 들어, 사람이 하나 이상의 그룹에 포함되어 있다면 `OU=Programmer,OU=Manager`와 같이 표현할 수 있습니다.

- **cn (Common Name)**: 오브젝트를 나타내는 이름 속성이다. 만약 사람에 관한 오브젝트라면 사람의 이름이 CN으로 표현될 수 있습니다.


## 예제
```ldap
dn: cn=John Doe,dc=example,dc=com
objectClass: inetOrgPerson
cn: John Doe
sn: Doe
givenName: John
mail: john.doe@example.com
```


##
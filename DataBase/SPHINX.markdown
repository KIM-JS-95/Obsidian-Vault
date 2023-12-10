# SPHINX


## What is sphinx ??


>Sphinx is an open source full text search server, designed from the ground up with performance, relevance (aka search quality), 
and integration simplicity in mind.
Sphinx lets you either batch index and search data stored in an SQL database, NoSQL storage, or just files quickly and easily 
— or index and search data on the fly, working with Sphinx pretty much as with a database server.
A variety of text processing features enable fine-tuning Sphinx for your particular application requirements, 
and a number of relevance functions ensures you can tweak search quality as well.
Searching via SphinxAPI is as simple as 3 lines of code, and querying via SphinxQL is even simpler, with search queries expressed in good old SQL.
Sphinx clusters scale up to tens of billions of documents and hundreds of millions search queries per day
>
> 스핑크스 공식 문서 


스핑크스 공식 문서에 따르면 `full text search` 검색방법을 지원하며 
- 심플하고 성능이 좋은 검색 서비스 기능을 지원
- RDBMS,NoSQL을 지원
- `SPHINX API`과 `SphinxQL`를 사용하여 빠르고 쉽게 쿼리를 구현
- 하루 수십건의 문서 및 쿼리 를 처리

를 특징으로 꼽고있다.

다른 블로그 혹은 스핑크스 사용자들이 스핑크스의 장점으로 Mysql 보다 빠른 `Full-text-search`를 이야기하고 있다.


><원문>
>
>It is a fundamental design difference. MySQL is designed around random access usage and
the ability to insert, update, delete, and read from tables virtually at will.
>
> Sphinx, however, is geared around the single task of text searching; its indexes are
designed with this in mind, not general purpose stuff. Note that when doing searches
against Sphinx indexes you don't get back your original row.
>
><번역 및 요약>
>
>Sphinx 는 기존 SQL 과는 다르게 `인덱스 설계에서 차이`가 난다.
Mysql의 경우 가상 테이블에 `Random Access`이지만 스핑크스의 경우 Single Text Searching을 염두하여 개발했다.
>
>단, 스핑크스의 검색 결과는 original 행을 반환하지 않는다.


요는 인덱싱 설계의 경우 멀티가 아닌 검색특화의 싱글 테스크를 염두하고 설계하였다는 것이며 
추가로 Mysql에서의 `Full-Text-Search`는 DataBase 엔진에 큰 부하가 생기기 때문에 부분적으로 Sphinx를 사용한다는 것였다.


## 스핑크스를 선택한 이유

자사 서비스 특성상 Text가 많은 부분을 차지하며 빠른 검색을 위해서는 단일 SQL을 통한 엔진 부하를 피해야했다.

특히 입력보다는 문서를 검색하는 일이 많아 검색에 특화된 Sphinx 엔진을 사용해야했고 
추가로 SQL의 Learning 이 쉬워 빠르게 개발하기 위해서 스핑크스를 도입하게 되었다.


## Mysql vs Sphinx

앞선 글에도 볼 수 있듯이 각자의 특화된 기능을 통해 많이 사용되고 있으며 두가지를 혼합하여 사용할 수 도있다.

SE 개발자가 아닌 BE개  발자로서 바라본 이 둘의 차이라면 쿼리문에 대해 이야기 하고싶다.

### 예시
```roomsql
-- Mysql
SELECT * FROM STUDENT 
    WHERE NAME LIKE "%이%";

SELECT * FROM STUDENT 
    WHERE NAME LIKE "%이%" AND ADDRESS LIKE "%이%";

-- Sphinx
SELECT * FROM STUDENT 
    WHERE MATCH(@name "이");

SELECT * FROM STUDENT 
    WHERE MATCH(@(name,address) "이");


```

Mysql 에서 `Match function`를 사용할 수 없는 것은 아니다.

그러나 필수 조건으로 해당 컬럼은 full-text 타임이 선언되어야하지만 스핑크스의 경우 조건 없이도 사용할 수 있다.

그러나 스핑크스에서는 Like 구문을 사용할 수 없고 대신 Match 구문만을 사용할 수 있다.


## 정말로 빠를까?

[Mysql vs Sphinx speed Test](https://www.percona.com/blog/2009/04/19/talking-mysql-to-sphinx/)

이 둘에 대한 테스트 결과를 많은 문서에서 찾아 볼 수 있다.


>Now on performance
> 
>– for given class of queries Sphinx was just 1.5-2 times faster. 
>
>I honestly hoped for more, though I carefully picked queries which are reasonably good for both of them 
>
>– it is easy to “break” MySQL making it to do group by with on disk temporary table 
which will make Sphinx much faster and few others.

수 만건의 데이터를 두고 단순 Select를 호출한다면 그 결과는 평균적으로 1.5배에서 2배의 빠른 속도를 보였다.

## 빠르다해서 결코 정확한 것은 아니다.

스핑크스는 `fulltext-search`를 기본으로 하며 `N-gram 알고리즘`이 기반이 된다.

`N-gram 알고리즘`은 연속된 단어를 찾아내는 알고리즘으로 다음과 같이 예로들 수 있다.

```
ABC, AB, BC
```

즉, 키워드 "[더뉴스]" 를 찾아낸다면 "더뉴스" 혹은 "더더뉴스" 가 포함된 컬럼이 검색될 가능성이 있다는 것이다.

때문에 스핑크스는 빠르지만 노이즈가 많은 SQL 이라는 말이 여기서 시작된 것이다.


# Reference
- [스핑크스 공식 홈페이지 - SPHINX DOCUMENT](https://sphinxsearch.com/about/sphinx/)
- [Why SpinxSql is faster than Mysql?](https://sphinxsearch.com/forum/view.html?id=2559)
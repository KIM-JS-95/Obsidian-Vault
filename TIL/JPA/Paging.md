# Spring Data 페이징

스프링 데이터는 JPA 쿼리 메소드에 페이징과 정렬 기능을 사용할 수 있도록 2가지 특별한 파라미터를 제공한다.

- org.springframework.data.Sort : 정렬기능
- org.springframework.data.Pageable : 페이징 기능 (Sort 포함)

## Page 타입

`Page` 메소드는 페이징 기능을 제공하기 위해 검색된 전체 데이터 컨수를 조회하는 `count` 쿼리를 추가로 호출한다.

```java
// count 쿼리 사용
Page<Member> findByName(String name, Pageable pageable);

// count 쿼리 사용 안 함
        List<Member> findByName(String name, Pageable pageable);

```

## 페이지 조건 걸기
```java
PageRequest pageRequest
        = new PageRequest(0, 10, new Sort(Direction.DESC, "name"));

        Page<Member> result = memberRepository.findByNameStartingWith("김", PageRequest);

        List<Member> members = result.get.getContent();

        int totalPages = result.getTotalPages();

        boolean hasNextPage - result.hasNextPage();

```


## My Project Code

```java
  @Transactional
public List<GallaryDto> getBoardlist(Integer pageNum) {

        Page<Gallary> page = gallaryRepository.findAll(PageRequest.of(pageNum-1, PAGE_POST_COUNT,
        Sort.by(Sort.Direction.ASC,"createDate")));


        List<Gallary> boards = page.getContent();

        List<GallaryDto> boardDtoList = new ArrayList<>();

        for(Gallary board : boards){
        boardDtoList.add(this.convertEntityToDto(board));
        }

        return boardDtoList;
        }

```

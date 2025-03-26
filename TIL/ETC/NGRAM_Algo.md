# Ngram Algorithm

## N-GRAM 개념

`N-gram`은 통계학 기반의 언어 모델중 하나로 다음 단어를 예측할 때 문장에서의 모든 단어를 고려하지 않고 특정 단어(TOKEN)의 개수(N)만 고려한다.

ex) “산에서 들개 떼를 만났다” 등산 사고 민원 예고 울렸다

|N|모델명|구현|
|:---:|:---:|:---:|
|1|Unigram|“산에서 / 들개 / 떼를 / 만났다” / 등산 / 사고 / 민원 / 예고 / 울렸다|
|2|Bigram|“산에서 들개 / 떼를 만났다” / 등산 사고 / 민원 예고 / 울렸다|
|3|Trigram|“산에서 들개 떼를 / 만났다” 등산 사고 / 민원 예고 울렸다|
|4|4-gram|“산에서 들개 떼를 만났다” / 등산 사고 민원 예고 / 울렸다|

```java
public class NGramGenerator {
    public static List<String> generateNGrams(String text, int n) {
        List<String> ngrams = new ArrayList<>();
        String[] words = text.split(" "); // 공백 기준으로 단어 분리
        
        if (n > words.length) {
            return ngrams; // 단어 개수가 N보다 작으면 빈 리스트 반환
        }
        
        for (int i = 0; i <= words.length - n; i++) {
            StringBuilder ngram = new StringBuilder();
            for (int j = 0; j < n; j++) {
                if (j > 0) ngram.append(" ");
                ngram.append(words[i + j]);
            }
            ngrams.add(ngram.toString());
        }
        
        return ngrams;
    }
```

## N-GRAM 고질적 문제

알고리즘을 적용할 경우 검색 속도는 개선되며 어떤 언어로든 구현할 수 있지만
반대로 의도하지 않은 검색 데이터가 검색될 수 도 있다.

실제 서비스에 적용하는 단계에 있어서는 정확한 그리고 의도한 결과가 나타나야 좋지만 `N-gram` 방식은 가능한 모두 가져다 준다.

> 너가 뭘 좋아할지 몰라 다 준비했어.

때문에 이러한 알고리즘을 적용한 스핑크스가 <u>노이즈가 많은 SQL</u> 이라는 말이 등장한 것이다.

ex) "들개"

의도) “산에서 <u>들개</u> 떼를 만났다” 등산 사고 민원 예고 울렸다...

결과) 이<u>들</u> <u>개</u>미가 발견된 컨테이너는 베트남 하이퐁에서 인천항을 통해 지난 10일 국내로 수입됐으며 21일 해당 물류센터로 옮겨졌습니다.


## 문제를 어떻게 해결할 것인가?

검색 서비스에 적용하기 위해서는 N-GRAM의 노이즈 문제를 해결해야한다.

1. N 의 수를 늘리자

2. TOKEN을 많이 가져가자


ex) "산에서 들개"

의도) “<u>산에서 들개</u> 떼를 만났다” 등산 사고 민원 예고 울렸다...

결과) “<u>산에서 들개</u> 떼를 만났다” 등산 사고 민원 예고 울렸다...


|-|Unigram|Bigram|Trigram|
|:---:|:---:|:---:|:---:|
|Perplexity|962|170|109|

`Perplexity`의 값이 작을 수록 좋은 성능을 나타내며 표에서 보듯 N의 값이 클수록 이상적인 결과를 볼수 있다.

## TOKEN을 늘리는 것이 항상 좋은 방향일까?

딥러닝 문서에서는 N이 커진다 하여 항상 좋은 결과를 보여주지 못한다고 말한다.

이를 `Trade-off`라고 하며 가장 좋은 결과를 보기 위해서는 N의 값을 1~4에서 지정하는 것이 가장 좋다고 한다.



# REFERENCE
- [딥러닝을 이용한 자연어 처리 입문](https://wikidocs.net/21692)
- [Elastic 가이드북](https://esbook.kimjmin.net/06-text-analysis/6.6-token-filter/6.6.4-ngram-edge-ngram-shingle#ngram)
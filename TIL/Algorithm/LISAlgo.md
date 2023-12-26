## Longest Increasing Subsequence(LIS)

최장 증가 부분 수열(Longest Increasing Subsequence) 문제는, 주어진 수열에서 오름차순으로 
정렬된 가장 긴 부분수열을 찾는 문제이다. 

여기서의 부분 수열은 연속적이거나 유일할 필요는 없다. 


최장 증가 부분 수열 문제는 입력 수열의 길이가 n일 때 **O(N^2)**의 시간에 풀이가 가능하다.


## 구현
### 1. 개념
증가 부분 수열을 만들기 위해서는 2중 loop 문(i, j)으로 순회하면서 하나의 i 이전까지 순열중에서 가장 긴 배열을 선택하면 된다.


![1](https://shoark7.github.io/assets/img/algorithm/lis-array1.png)

![2](https://shoark7.github.io/assets/img/algorithm/lis-array2.png)

모든 index를 순회하면서 각 인덱스의 LIS는 다음과 같다. 
최종적으로 위 배열에서 LIS 값은 4 이다.

|Index(i)|arr|Index(i)|arr|
|:---:|:---:|:---:|:---:|
|i=0|{1}|i=4|{1,4,6,8}|
|i=1|{1,4}|i=5|{1,4,6,8}|
|i=2|{1,4,6}|i=6|{1,4,6,8}|
|i=3|{1,4,6,8}|i=7|{4,5,6,7}|

### 2. 위 문제로 도출해 낼 수 있는 공식은?
1. 정수 i, j에 대해 i < j이면, S[i] < S[j]다.(0 <= i, j <= |S|)
2. 정수 i, j에 대해 S[i] < S[j]이면, 원 배열 arr에서의 S[i], S[j] 두 수의 위치 전후관계는 같다.(0 <= i, j <= |S|)


### LIS 구현하는 2가지 방법([with. 가장 긴 증가하는 부분 수열](https://www.acmicpc.net/problem/11053))

#### 1. 동적 계획법

주어진 arr 배열에서 조건에 적합한 dp 배열을 채워 나가는 방법으로 시간 복잡도는 **O(N^2)** 이다.

```python
class Solution :
    def LIS(self, nums: List[int]) -> int:
        dp = [0 for i in range(n)]
        for i in range(n):
            for j in range(i):
                if a[i] > a[j] and dp[i] < dp[j]:
                    dp[i] = dp[j]
            dp[i] += 1
    return max(dp)
```


#### 2. 이진탐색
시간복잡도는 O(NlogN)

```python
class Solution :
    def LIS(self, nums: List[int]) -> int:
        
        dp = [arr[0]]
        for i in range(x):
            if arr[i] > dp[-1]:
                dp.append(arr[i])
            else:
                idx = bisect.bisect_left(dp, arr[i])
                dp[idx] = arr[i]

    return len(dp)

```

### 🧾Reference
1. [최장 증가 부분 수열](https://ko.wikipedia.org/wiki/%EC%B5%9C%EC%9E%A5_%EC%A6%9D%EA%B0%80_%EB%B6%80%EB%B6%84_%EC%88%98%EC%97%B4)
2. [이것이 코딩 테스트다](https://github.com/ndb796/python-for-coding-test)
3. [LIS 구현하는 3가지 방법](https://gusudss.tistory.com/44)
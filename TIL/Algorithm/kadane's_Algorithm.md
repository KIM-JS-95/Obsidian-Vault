[[0-Algorithm MOC.md]] · #algorithm <!-- moc-nav -->

## 최대 부분 합 구하기

1차원 배열에서 가장 큰 값을 가질 수 있는 `연속적인 부분 배열`을 찾는 문제에 사용되는 알고리즘이다.

많은 문제들이 시간, 공간 복잡성이 적은 `카디안 알고리즘`을 적용한 문제 풀이를 선호한다.

카디안 알고리즘에서는 시,공간 복잡성이 **O(n)** 으로 다음과 같이 구현한다.


[LeetCode 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) 문제 링크
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        csum = 0

        for i in nums:
            csum +=i
            if csum > ans:
                ans = csum
            if csum < 0:
                csum = 0
        return ans
```
전 배열을 순회하면서 값을 하나씩 더해 현재 위치 까지의 배열의 최대 값과 비교하여 더 큰값을 가져간다.

확인해야 할 점은 배열에 음수 값이 존재한다는 점으로 sum 값을 구할 때 마다 0보다 작을 경우 0으로 바꾸어 주어야한다.


![](https://assets.leetcode.com/users/images/2715e7ab-8fad-4f5f-ace9-cfe83acba68f_1637809592.7767313.jpeg)


### 🧾Reference
[카데인 알고리즘](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)
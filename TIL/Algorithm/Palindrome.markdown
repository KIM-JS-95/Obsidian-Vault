## 목표
 앞뒤가 똑같은 숫자를 확인해보자

### Palindrome

변수 타입에 상관없이 변수를 역전후 초기값과 비교하면된다.

`반복문`을 사용하여

```text
ex) x =123;

int temp
=> 3 -> 30 + 2 -> 300 + 20 + 1

```

요런식으로 계산하면 된다.

```java
class Solution {
    public boolean isPalindrome(int x) {
     
        if(x<0 || (x!=0 && x%10==0)) return false;
        
        int num=0;
        int temp =x;
       while(temp>num){
        num=num*10+temp%10;
        temp/=10;
        }
        
       // System.out.println(ans);
        
        return ((num==temp) || (num/10)==temp);
    }
}
```


### Linked List 문제는 어떻게 접근할까?
Linked List 문제의 경우에는 내부 변수가 `Integer` 타입이며 
만일 Integer 범위에서 벗어나는 값이 입력될 경우 값이 OverFlow 되어 문제를 해결할 수 없다.

문제는 LinkedList이다.
변수 선언후 시작 부분과 끝부분의 값이 모두 동일하다면 `Palindrome`이 성립된다.

여기서 LinkedList l1은 배열의 마지막으로 이동시키기 위해 재귀를 사용했다.

![KakaoTalk_20220114_180038804](https://user-images.githubusercontent.com/65659478/149488221-9fc6df60-8364-485a-91c3-a40afff9f711.jpg)

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
     ListNode l2;
    public boolean isPalindrome(ListNode head) {
        l2 = head;
        return solve(head);
    }
    
    boolean solve(ListNode l1 ){
        if(l1 == null)
            return true;
        
        boolean prevAns = solve(l1.next);
        
        boolean ans = prevAns && (l1.val == l2.val) ;
        l2 = l2.next;
        return ans;
        
    } 
}
```

## 관련 포스팅 (LeetCode)
* [Palindrome Number](https://leetcode.com/problems/palindrome-number/)
* [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

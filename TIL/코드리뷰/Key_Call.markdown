# 매번 까먹는 HashMap Key, Value 호출

해시맵은 Key값으로 Value 값을 호출하는 것은 가능하지만 그 반대는 지원하지 않는다.

그래서 별도로 코드 작성을 할 줄 알아야한다.

알고리즘 테스트에서 이거 몰라서 난감한 경우가 많았다.

## 방법은 많다.

- map.entrySet()
- map.keySet(), Iterator
- entrySet()
- forEach (Java 8 이후)

## map.entrySet()

```java
public class HashMapPrint {
    public static void main(String[] args) {
// HashMap 준비
        Map<Integer, String> map = new HashMap<Integer, String>();
        map.put(1, "Apple");
        map.put(2, "Banana");
        map.put(3, "Orange");
// for loop (entrySet())
        for (Entry<Integer, String> entrySet : map.entrySet()) {
            System.out.println(entrySet.getKey() + " : " + entrySet.getValue());
        }
    }
}

```

### map.keySet(), Iterator

이 방식은 해쉬맵이 가지고 있는 키 값만을 호출하는 방식이다.

```java
public class MapSample {
    public static void main(String[] args) {
        Map<String, Integer> hashMap = new HashMap<String, Integer>();
        hashMap.put("Key1", 1);
        hashMap.put("Key2", 2);
        hashMap.put("Key3", 3);

        Set set = hashMap.keySet();
        Iterator iterator = set.iterator();
        while (iterator.hasNext()) {
            String key = (String) iterator.next();
            System.out.println("KEY : " + key);
        }
    }
}
```


### forEach (Java 8 이후)

```java
import java.util.HashMap;
import java.util.Map;

public class HashMapPrint {
    public static void main(String[] args) {
// HashMap 준비
        Map<Integer, String> map = new HashMap<Integer, String>();
        map.put(1, "Apple");
        map.put(2, "Banana");
        map.put(3, "Orange");
// forEach
        map.forEach((key, value) -> {
            System.out.println(key + " : " + value);
        });
    }
}

```

## Value 값으로 Key 값 찾기

```java

public class HashMapPrint {
    public static void main(String[] args) {
    // HashMap 준비
        Map<Integer, String> map = new HashMap<Integer, String>();
        map.put(1, "Apple");
        map.put(2, "Banana");
        map.put(3, "Orange");

    }
    
    public static<K, V> K getKey(Map<K, V> map,V value){

        for(K key:map.keySet()){
            if(value.equals(map.get(key))){
                return key;
            }
        }
        return null;
    }
}
```

## entrySet() (งᓀ‸ᓂ)ง keySet()

`entrySet()`은 키값 ,Value 값 모두 가져옴

`keySet()`은 키값만 가져옴

## Reference

- [나만의 기록들](https://mine-it-record.tistory.com/233)
- [어제 오늘 내일](https://hianna.tistory.com/573)
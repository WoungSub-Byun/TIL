# Heap sort - 힙 정렬
---

## 개념

**그전에, 힙(heap)자료구조는?**
### Heap
완전 이진트리의 하나로 우선순위 큐를 위해 만들어진 자료구조
- **내림차순 정렬**
최대 힙 구성
- **오름차순 정렬**
최소 힙 구성

## 특징
- 짧은 시간 복잡도
- **최댓/최소값이 필요할 때 가장 유용하게 쓰인다**

> 시간 복잡도
O(nlog₂n)


## 구현
Python에서는 heapq 라이브러리를 사용하여 손쉽게 구현이 가능하다

```python

import heapq

# 오름차순 정렬
def min_heap(arr):
    return heapq.heapify(arr)

# 내림차순 정렬
def max_heap(arr):
    result = []
    for i in arr:
        heapq.heappush(result, (-i, i)) #우선순위, 값
    return result[1:] #계산의 용이를 위해 0번쨰 인덱스는 사용하지 않습니다.
```

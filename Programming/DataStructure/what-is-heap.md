# Heap
------

## 개념
완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조이다. 여러개의 값들 중에서 최댓값이나 최솟값을 빠르게 찾아내도록 만들어진 자료구조이다. 

**종류**
- **최대 힙(Max Heap)**
부모 노드의 키 값이 자식노드의 키값보다 크거나 같은 완전 이진 트리
- **최소 힙(Min Heap)**
부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진 트리

![heapimage](./../Image/heapmaxmin.png)


## 구현

- 힙에서의 부모노드와 자식 노드의 관계
    - 왼쪽 자식의 인덱스 = 부모 인덱스 * 2
    - 오른쪽 자식의 인덱스 = 부모 인덱스 * 2 + 1
    - 부모 인덱스 = 자식 인덱스 / 2

![heapindex](./../Image/heapindex.png)


> **Python에서는 heapq 라이브러리를 통해 쉽게 구현할 수 있다**

### 삽입

![maxheapimg](./../Image/maxheapimg.png)

```python
import heapq
arr = [1,9,7,4,3]
node = 2 #추가할 값
heapq.heappush(node, arr)
```



### 삭제
![heapremove](./../Image/heapremove.png)

```python
import heapq
arr = [1,9,7,4,3]
heapq.heappop(arr)
```
# Insert Sorting - 삽입 정렬
---

## 개념
매 순서마다 이미 정렬된 배열 부분에서 해당 원소를 삽입할 수 있는 위치를 찾아 해당 위치에 넣는다.

## 특징
- 안정된 정렬 방법
- 대부분의 레코드가 이미 정렬되어 있는 경우 매우 효율적
- 비교적 많은 레코드들의 이동을 포함
- 레코드 수가 많고 레코드 크기가 클 경우에 적합하지 않다.

> 시간 복잡도
**O(n^2)**

## 예시
![insertsort](./../../Image/insertsort.png)

## 구현
```python
# 오름차순 정렬
def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[i - 1], arr[j] = arr[j], arr[j + 1]

```

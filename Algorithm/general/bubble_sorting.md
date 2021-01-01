# Bubbling Sorting - 버블 정렬
---

## 개념
서로 인접한 두 원소를 검사하여 정렬하는 알고리즘

## 특징
- 구현이 매우 간단
- 하나의 요소가 가장 왼쪽에서 가장 오른쪽으로 이동하기 위해서는 배열에서 모두 다른 요소들과 교환되어야 한다.
- 특정 요소가 최종 정렬 위치에 있는 경우라도 교환되는 일이 일어난다.

> 시간 복잡도
    **O(n^2)**

* 😡**높은 시간복잡도 때문에 간단한 구현에도 불구하고 잘 사용되지 않는다.**

## 예시
![bubblesort](./../../Image/bubblesort.png)


## 구현
```python
# 오름차순 정렬
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr), i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```
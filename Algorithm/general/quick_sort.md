# Quick Sort - 퀵 정렬
---

## 개념
*불안정 비교 정렬*에 속하며, **피벗**을 기준으로 피벗보다 작은 요소들은 모두 왼쪽으로 옮겨지고(*오름차순기준*) 피벗보다 큰 요소들은 모두 피벗의 오른쪽으로 옮겨 분할된 부분 리스트에 대해 **순환 호출**을 이용하여 정렬을 반복하고 더이상 분할이 불가능할 때까지 반복하여 정렬하는 방법이다.
> **피벗 - Pivot**
리스트 안의 임의의 값, 대체로 첫번째 원소를 기준으로 한다.

**단계**
- **분할(Divide)**
입력 배열을 피벗을 기준으로 비균등하게 2개의 부분배열로 분할
- **정복(Conquer)**
    - 부분 배열을 정렬
    - 부분배열의 크기가 0이나 1이 될때까지 **순환호출**을 이용하여 분할 정복을 적용
- **결합(Combine)**
정렬된 부분 배열들을 하나의 배열에 합병

> 😉 **순환호출이 한번 진행될 때마다 최소한 하나의 원소(피벗)는 최종적으로 위치가 정해지므로, 이 알고리즘은 반드시 끝난다는 것을 보장할 수 있다.**


## 특징
- **😀분할 정복(divide and conquer) 방법**
    - 문제를 작은 2개의 문제로 분리하고 각각을 해결한 다음, 결과를 모아서 원래의 문제를 해결하는 전략

## 예시
![quicksort](./../../Image/quicksort.png)

## 구현
```python
#오름차순
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] #리스트의 중간 값을 피벗으로 지정
    low, equal, high = [], [], []
    for i in arr:
        if i > pivot:
            low.append(i):
        elif i < pivot:
            high.append(i):
        else:
            equal.append(i)
    return quick_sort(low) + equal + quick_sort(high)

```
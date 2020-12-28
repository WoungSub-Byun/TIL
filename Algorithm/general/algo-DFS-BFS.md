# DFS/BFS
---


## Before DFS/BFS...
---
### Stack
- LIFO의 형태를 가지는 자료구조
[Stack-TIL-Link](https://github.com/icefirebear/TIL/blob/main/DataStructure/what-is-stack.md)
### Queue
- FIFO의 형태를 가지는 자료구조
[Queue-TIL-Link](https://github.com/icefirebear/TIL/blob/main/DataStructure/what-is-queue.md)
### Recursive Function
자기 자신을 다시 호출하는 함수
```python
def recursive_func():
    print("recursive")
    recursive_func()
```
>*RecursionError: maximum recursion depth exceeded while calling a Python object*
- Python에서는 재귀 제한 깊이를 두어 함수가 일정 횟수 이상 재귀적으로 호출된다면 RecursionError가 발생한다.

재귀함수를 문제풀이에서 사용할 때에는 종료조건을 반드시 명시해야 한다.

> 팩토리얼 구현 예제
```python
# 단순 반복
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Recursive
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)
```

> 💡 **유클리드 호제법 - GCD 계산**
- GCD: Greatest Common Divisor - 최대공약수

두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 한다면 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.

```python
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        gcd(b, a%b)
```

이처럼 재귀함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있다.
> 하지만 가독성있는 코드를 짜기에는 좋지 않은 방법이기때문에 상황에 맞추어 잘 사용하자

## DFS - Depth-First Search

## BFS - Breadth First Search

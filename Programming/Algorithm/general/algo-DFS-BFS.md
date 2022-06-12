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

✔ **깊이 우선 탐색**
현재 정점과 연결된(인접한) 정점들을 갈 수 있는지 검사하고, 특정 정점으로 갈 수 있다면 그 정점에 가서 같은 행위를 반복하는 탐색 알고리즘

> **장점**
- 직관적이고 구현하기 쉬움
- 같은 정점을 반복하지 않도록 정점에 방문했다는 것을 표시해준다.
- 재귀함수를 통해 구현한다.

> **단점**
- 재귀함수를 이용하기 때문에, 함수 호출 비용이 추가로 들어간다.
- 재귀 깊이가 지나치게 깊어지면 메모리 비용을 예측하기 어렵다.
> 재귀를 할 때마다 호출된 함수의 수만큼 스택메모리에  쌓이게 되는데 재귀 깊이가 깊어진다면 스택메모리에 쌓이는 양이 비례적으로 많아져 메모리가 펑하고 터질 수도 있다.
- 최단 경로를 알 수 없다.


![dfsbfsimage](https://miro.medium.com/max/4436/1*exRbhrS8p9YZAovBYPgzKg.png)

## BFS - Breadth First Search
✔ **너비 우선 탐색**
시작점에서 가까운 정점부터 순서대로 방문하는 탐색 알고리즘 

> **장점**
- 효율적인 운영 가능
- 시간/공간 복잡도 면에서 안정적
- 간선의 비용이 모두 같을 경우, 최단 경로를 구할 수 있다.
    > 간선의 비용이 같다?
    문제의 조건에서 경로마다 비용이 다르게 주어지는 경우가 있는데 이런 경우에는 다익스트라 알고리즘 등의 최단거리 알고리즘을 활용해야 한다.

> **단점**
- DFS에 비해 코드 구현이 어렵다.
- 모든 지점을 탐색할 경우를 대비해, 큐의 메모리가 미리 준비되어 있어야 한다.

> DFS vs BFS
- 메모리 관리
=> 기본적으로 드는 메모리 비용은 BFS가 많지만, DFS는 예외적인 상황에서 더 많은 메모리 비용이 든다.
# BFS - 너비 우선 탐색
---
- 너비 우선 탐색이라고 부르는 BFS 알고리즘에 대해서 알아보겠습니다.


## 개념
---
### 너비 우선 탐색
**BFS - Breadth First Search**
![bfsimage](https://hackr.io/blog/media/architecture-of-bfs.png)

**인접한 노드부터 하나씩 탐색**하는 알고리즘이다.
- BFS는 큐(Queue)를 사용하여 구현한다.

**특징**
- **큐-Queue**를 사용하여 구현한다.
- *일반적인 경우 실제 수행 시간은 DFS보다 좋은 편*이다.


**탐색 과정**
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다.
3. 2번의 과정을 더 이상 수행할 수 없을 떄까지 반복한다.

**구현**
* Python에서는 deque라이브러리를 사용하는 것이 좋다.
```python
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start]) #큐를 만들고 시작 노드를 큐에 집어넣는다.
    visited[start] = True #시작 노드를 방문처리한다.

    while queue: 
        v = queue.popleft() # 큐의 가장 아래에 있는 노드를 pop한다.
        print(v, end=' ') # 노드를 출력한다.

        for node in graph[v]: #출력한 노드에 인접한 노드들을 확인한다.
            for not visited[node]: #인접한 노드의 방문처리여부를 확인한다.
                queue.append(node) #방문처리되지 않았다면 큐에 넣고
                visited[node] = True #방문처리해준다.

# BFS는 
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9
bfs(graph, 1, visitied) #그래프, 시작노드, 방문처리할 배열
```
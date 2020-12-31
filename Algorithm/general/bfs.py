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

bfs(graph, 1, visited) #그래프, 시작노드, 방문처리할 배열
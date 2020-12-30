def dfs(graph, v, visited):
    #V : 현재 노드
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited) #현재 노드와 인접한 다른 노드를 재귀적으로 방문
    
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
# 최상단 노드 1
dfs(graph, 1, visited)
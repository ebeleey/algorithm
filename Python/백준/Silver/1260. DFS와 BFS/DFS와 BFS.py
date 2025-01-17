N, M, v = map(int, input().split()) # N: 노드 개수, M: 간선 개수, V: 시작 노드

datas = [list(map(int, input().split())) for _ in range(M)] # 간선이 연결하는 두 노드의 번호

# 인접 리스트 만들기
def adjacency_list(datas, N):
    matrix = [[] for _ in range(N+1)]

    for data in datas:
        i, j = data
        matrix[i].append(j)
        matrix[j].append(i)
        matrix[i].sort()
        matrix[j].sort()
    return matrix

graph = adjacency_list(datas, N)
# print(graph)

visited = [False] * (N+1)

# DFS
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    # print(graph[v])
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, v, visited)
print()

from collections import deque

# BFS
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = False # 방문 처리 저장 리스트 재활용하기(반대로 저장)
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if visited[i]: #방문안했으면(반대니깐 not 안 씀)
                queue.append(i)
                visited[i] = False

bfs(graph, v, visited)
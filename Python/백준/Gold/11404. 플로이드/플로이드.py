import sys

n = int(sys.stdin.readline()) # 도시의 개수 n
m = int(sys.stdin.readline()) # 버스의 개수 m

inf = int(1e9)
graph = [[inf] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == inf:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
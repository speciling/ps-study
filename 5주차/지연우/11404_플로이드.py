import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
graph = [[float('inf')]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)
for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for g in graph:
    for i in range(n):
        if g[i] == float('inf'):
            g[i] = 0
    print(*g)
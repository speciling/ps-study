import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = [[INF] * n for _ in range(n)]

for i in range(n):
    for j,v in enumerate(list(map(int,input().split()))):
        if v == 1 :
            graph[i][j] =1 

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()
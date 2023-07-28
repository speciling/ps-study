import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = [[INF] * n for _ in range(n)]

# i에서 j까지의 경로가 있는 경우 graph[i][j] 값 1로 초기화
for i in range(n):
    for j,v in enumerate(list(map(int,input().split()))):
        if v == 1 :
            graph[i][j] =1 

# 플로이드 워셜 알고리즘 적용
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# graph[i][j] 값이 INF인 경우 경로가 존재하지 않으므로 0 출력
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()
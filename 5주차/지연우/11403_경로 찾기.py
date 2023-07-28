graph = [input().split() for _ in range(int(input()))]
for m in range(n:=len(graph)):
    for s in range(n):
        for e in range(n):
            if graph[s][e] == '0' and graph[s][m] == '1' and graph[m][e] == '1':
                graph[s][e] = '1'
for i in graph:
    print(*i)
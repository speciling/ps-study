from collections import deque
a, b, c = map(int, input().split())
graph = [[], ]
for _ in range(a):
    graph.append([])
visited = [False] * (a+1)
visited2 = [False] * (a+1)
for _ in range(b):
    num, com = list(map(int, input().split()))
    for i in range(1, a+1):
        if i == num:
            graph[i].append(com)
        if i == com:
            graph[i].append(num)
def dfs(graph, i, visited):
    visited[i] = True
    print(i, end=' ')
    for j in sorted(graph[i]):
        if not visited[j]:
            dfs(graph, j, visited)
def bfs(graph, i, visited2):
    queue = deque([i])
    visited2[i] = True
    while queue:
        j = queue.popleft()
        print(j, end=' ')
        for num in sorted(graph[j]):
            if not visited2[num]:
                queue.append(num)
                visited2[num] = True
dfs(graph, c, visited)
print()
bfs(graph, c, visited2)

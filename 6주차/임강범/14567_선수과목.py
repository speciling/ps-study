import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

result = [0] * (n+1)
q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        result[i] = 1

while q:
    now = q.popleft()
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            result[i] = result[now] + 1
            q.append(i)

print(*result[1:])
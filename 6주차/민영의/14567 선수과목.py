from collections import deque
import sys
input = sys.stdin.readline
a, b = map(int, input().split())
arr = [0] * (a+1)
graph = [[] for _ in range(a+1)]
for _ in range(b):
    c, d = map(int, input().split())
    graph[c].append(d)
    arr[d] += 1
answer = [1] * (a+1)
def topology_sort():
    result = []
    q = deque()
    for i in range(1, a+1):
        if arr[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for j in graph[now]:
            arr[j] -= 1
            if arr[j] == 0:
                q.append(j)
            answer[j] = answer[now] + 1
    print(*answer[1:])
topology_sort()

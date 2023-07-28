import heapq
import sys

input = sys.stdin.readline
a, b, c, d = map(int, input().split())
graph = [[] for _ in range(a + 1)]
INF = int(1e9)
for _ in range(b):
    e, f = map(int, input().split())
    graph[e].append((f, 1))
def dijkstra(start):
    distance = [INF] * (a + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance
ans = dijkstra(d)
arr = []
for j in range(1, a + 1):
    if c == ans[j]:
        arr.append(j)
if len(arr) != 0:
    for k in arr:
        print(k)
else:
    print(-1)

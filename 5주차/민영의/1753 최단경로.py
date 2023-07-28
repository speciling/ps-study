import heapq
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = int(input())
INF = int(1e9)
d = [INF] * (a+1)
arr = []
graph = [[] for _ in range(a+1)]

for _ in range(b):
    e, f, g = map(int, input().split())
    graph[e].append((g, f))
def dijkstra(start):
    d[start] = 0
    heapq.heappush(arr, (0, start))
    while arr:
        i, j = heapq.heappop(arr)
        if d[j] < i:
            continue
        for k, l in graph[j]:
            next = k + i
            if next < d[l]:
                d[l] = next
                heapq.heappush(arr, (next, l))
dijkstra(c)
for i in d[1:]:
    if i != INF:
        print(i)
    else:
        print("INF")

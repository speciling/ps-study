import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

v, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

distance = [INF]*(v+1)

q = []
heapq.heappush(q, (0,start))
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
print(*[i if i != INF else 'INF' for i in distance[1:]], sep='\n')
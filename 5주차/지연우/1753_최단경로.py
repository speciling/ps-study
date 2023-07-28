import sys, heapq
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
graph = [{} for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    if b not in graph[a] or c < graph[a][b]:
        graph[a][b] = c

dist = [float('inf')]*(v+1)
dist[k] = 0
q = [(0, k)]
while q:
    d, now = heapq.heappop(q)
    if d > dist[now]:
        continue
    for i, w in graph[now].items():
        if d+w < dist[i]:
            dist[i] = d+w
            heapq.heappush(q, (dist[i], i))

print('\n'.join(map(lambda x: str(x).upper(), dist[1:])))
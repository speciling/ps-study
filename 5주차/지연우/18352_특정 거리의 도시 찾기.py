import sys, heapq
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [float('inf')]*(n+1)
dist[x] = 0
q = [(0, x)]
while q:
    d, now = heapq.heappop(q)
    if d>dist[now]:
        continue
    for i in graph[now]:
        if d+1 < dist[i]:
            dist[i] = d+1
            heapq.heappush(q, (d+1, i))

ans = [str(i) for i, n in enumerate(dist) if n==k]
print('\n'.join(ans) or -1)
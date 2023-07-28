import sys, heapq
input = sys.stdin.readline

n, m = int(input()), int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

x, y = map(int, input().split())
costs = [float('inf')]*(n+1)
costs[x] = 0
q = [(0, x)]
while q:
    cost, now = heapq.heappop(q)
    if cost > costs[now]:
        continue
    elif now == y:
        break
    for i, c in graph[now]:
        if cost+c < costs[i]:
            costs[i] = cost+c
            heapq.heappush(q, (costs[i], i))
print(costs[y])
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

# 입력값으로 graph 작성
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c)) # a에서 b까지의 비용 c 

start, end = map(int,input().split())
distance = [INF] * (n+1)
q = []
heapq.heappush(q, (0,start)) 
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist: # 이미 방문했다면 스킵
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))
print(distance[end])
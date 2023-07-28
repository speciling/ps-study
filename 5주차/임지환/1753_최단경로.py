import heapq 
import sys 

Inf = int(1e9) 
input = sys.stdin.readline 
v, e = map(int, input().split()) 
distances = [Inf] * (v + 1) 
graph = [[] for _ in range(v + 1)]
start = int(input())  
for _ in range(e): 
    a, b, c = map(int, input().split()) 
    graph[a].append((b, c)) 
def djikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
djikstra(start) 
for i in range(1, v + 1):  
    if distances[i] == Inf: 
        print("INF") 
    else: 
        print(distances[i]) 

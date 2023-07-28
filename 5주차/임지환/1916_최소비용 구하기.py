import sys
import heapq

def dijkstra(start):
    distance[start] = 0
    h = []
    heapq.heappush(h, [distance[start], start])

    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                heapq.heappush(h, [cost, x[0]])
                distance[x[0]] = cost


input = sys.stdin.readline
n = int(input())
m = int(input())
array = [list(map(int, input().split())) for _ in range(m)] 
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF for _ in range(n+1)]
for i in range(m):
    departure, arrival, cost = array[i]
    graph[departure].append([arrival, cost])
start, end = map(int, input().split())

dijkstra(start)
print(distance[end])

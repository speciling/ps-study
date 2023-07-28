import heapq
import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
arr = [[] for _ in range(a+1)]

for i in range(b):
    c, d, e = map(int, input().split())
    arr[c].append([d, e])
c, d = map(int, input().split(' '))

dist = [int(1e9)] * (a+1)
q = []
dist[c] = 0
heapq.heappush(q, [0, c])

while q:
    cost, m = heapq.heappop(q)
    if cost > dist[m]:
        continue
    for i, j in arr[m]:
        distance = cost + j
        if distance < dist[i]:
            dist[i] = distance
            heapq.heappush(q, [distance, i])
print(dist[d])

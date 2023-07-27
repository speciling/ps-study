#!/usr/bin/env python
# coding: utf-8

# In[15]:


import heapq
import sys

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist +i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
                
inf = int(1e9)
n,m,k,x = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [inf]*(n+1)
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append((b,1))
dijkstra(x)

specificDis = []
for i in range(n+1):
    if distance[i] == k:
        specificDis.append(str(i))

if specificDis:
    print('\n'.join(specificDis))
else:
    print(-1)


# In[ ]:





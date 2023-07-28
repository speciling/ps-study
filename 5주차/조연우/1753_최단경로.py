#!/usr/bin/env python
# coding: utf-8

# In[45]:


import heapq
import sys
v,e = map(int, input().split())
s = int(input())
inf = int(1e9)
graph = [[] for i in range(v+1)]
distance = [inf]*(v+1)
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())  
    graph[a].append((b,c))
# 다익스트라 알고리즘
def dijkstra(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:   
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
dijkstra(s)
for i in range(1,v+1):
    if distance[i]==inf:
        print('INF')
    else:
        print(distance[i])


# In[ ]:





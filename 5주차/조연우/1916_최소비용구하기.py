#!/usr/bin/env python
# coding: utf-8

# In[26]:


import heapq
import sys
n,m = int(input()), int(input())
inf = int(1e9)
graph = [[] for i in range(n+1)]
distance = [inf]*(n+1)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
start, dest = map(int,input().split())
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
dijkstra(start)
print(distance[dest])


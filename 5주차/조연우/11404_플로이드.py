#!/usr/bin/env python
# coding: utf-8

# In[47]:


import sys
inf = int(1e9)
n, m = int(input()), int(input()) 
graph = [[inf] * (n+1) for _ in range(n+1)] 

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0
# 같은 a,b가 존재하는 경우 조건추가 
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if graph[a][b]<c:
        pass
    else:
        graph[a][b] = c
# 플로이드워셜알고리즘
for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == inf:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()


# In[ ]:





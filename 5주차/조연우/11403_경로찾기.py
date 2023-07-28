#!/usr/bin/env python
# coding: utf-8

# In[24]:


import sys
inf = int(1e9)
n = int(input())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)] 
# 경로가 없으면 무한으로 바꾸기
for i in range(n):
    for j in range(n):
        if graph[i][j]==0:
            graph[i][j] = inf
# 플로이드 워셜 알고리즘
for k in range(0,n):
    for a in range(0, n):
        for b in range(0,n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
# 출력
for a in range(0,n):
    for b in range(0,n):
        if graph[a][b] == inf:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()  


# In[ ]:





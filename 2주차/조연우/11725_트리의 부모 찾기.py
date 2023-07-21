#!/usr/bin/env python
# coding: utf-8

# In[15]:


import sys
sys.setrecursionlimit(10**6)
def dfs(n):
    for i in link[n]:
        if srt[i] == 0 :
            srt[i] = n
            dfs(i)
n = int(input())
link = [[] for _ in range(n+1)]
srt = [0]*(n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    link[a].append(b)
    link[b].append(a)
dfs(1)
for i in range(2,n+1):
    print(srt[i])


# In[ ]:





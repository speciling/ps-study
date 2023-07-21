#!/usr/bin/env python
# coding: utf-8

# In[4]:


count=0
def dfs(n):
    global count
    ch[n]=1
    for i in link[n]:
        if ch[i]==0:
            dfs(i)
            count+=1
            
n = int(input())
ln = int(input())
ch = [0]*(n+1)
link = [[] for _ in range(n+1)]
for _ in range(ln):
    a,b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)
dfs(1)
print(count)


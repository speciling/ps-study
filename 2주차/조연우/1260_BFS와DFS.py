#!/usr/bin/env python
# coding: utf-8

# In[4]:


def dfsd(n):
    dfs.append(n)
    for i in link[n]:
        if i not in dfs:
            dfsd(i)
def bfsd(n):
    q=[n]
    while q:
        for i in link[q.pop()]:
            if i not in bfs:
                bfs.append(i)
                q.insert(0, i)



n, m, v = map(int,input().split())
link=[[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    link[a].append(b)
    link[b].append(a)
for i in range(1,n+1):
    link[i].sort()
dfs = []
bfs = [v,]
dfsd(v)
bfsd(v)
print(*dfs)
print(*bfs)


# In[ ]:





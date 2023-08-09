#!/usr/bin/env python
# coding: utf-8

# In[10]:


import sys
input = sys.stdin.readline

def find_parent(parent, x): 
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) 
    return parent[x]

def union_parent(parent,a,b): 
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
n, m = map(int, input().split())
parent = [0]*(n+1)
for i in range(1, n+1): 
    parent[i] = i  

cycle = False
answer=[]
for i in range(m):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        answer.append(i+1)
    else:
        union_parent(parent, a, b)
        
if cycle:
    print(answer[0])
else:
    print(0)


# In[7]:





# In[ ]:





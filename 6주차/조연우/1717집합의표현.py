#!/usr/bin/env python
# coding: utf-8

# In[8]:


import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def find_parent(parent, x): # 루트노드찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) 
    return parent[x]

def union_parent(parent,a,b): # 두 원소가 속한 집합을 함치기
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
    
for _ in range(m):
    k, a, b = map(int, input().split())
    if k == 0:
        union_parent(parent, a, b)
    elif k == 1:
        find_parent(parent, a)
        find_parent(parent, b)
        if parent[a]==parent[b]:
            print('YES')
        else:
            print('NO')
        


# In[ ]:





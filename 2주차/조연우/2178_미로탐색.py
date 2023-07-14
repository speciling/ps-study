#!/usr/bin/env python
# coding: utf-8

# In[39]:


from collections import deque
def bfs():
    global m,n, count
    while lst: 
        xy = lst.popleft()
        x=xy[0]
        y=xy[1]
        if x==m-1 and y==n-1:
            return
        for i in range(4):
            if 0<=x+xd[i]<n and 0<=y+yd[i]<m:
                if mirror[x+xd[i]][y+yd[i]]==1:
                    nx = x+xd[i]
                    ny = y+yd[i]
                    mirror[nx][ny]=mirror[x][y]+1
                    lst.append([nx,ny])
            
                

n,m = map(int,input().split())
mirror = [ list(map(int,(list(input())))) for _ in range(n)]
xd = [1,-1,0,0]
yd = [0,0,1,-1]
lst=deque([[0,0]])
bfs()
print(mirror[n-1][m-1])


#!/usr/bin/env python
# coding: utf-8

# In[4]:


def dfs(x,y):
    global n, count
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if mapp[x][y] == 1:
        count += 1
        mapp[x][y]=0
        for i in range(4):
            nx = x+dirx[i]
            ny = y+diry[i]    
            dfs(nx,ny)               
# 인덱스 밖인 경우 리턴
# 인덱스 내에 1인경우 전체수+1, 0으로바꾸기, nxny만들어서dfs
            
dirx = [1,-1,0,0]
diry = [0,0,1,-1]
count = 0
lst = []
n = int(input())
mapp = [list(map(int,list(input()))) for _ in range(n)]
# 방향키와 2차원 배열

for i in range(n):
    for j in range(n):
        if mapp[i][j] == 1:
            count = 0
            dfs(i,j)
            lst.append(count)
# 1나오면 dfs돌리기
            
print(len(lst))
lst.sort()
for i in lst:
    print(i)
# 출력


# In[ ]:





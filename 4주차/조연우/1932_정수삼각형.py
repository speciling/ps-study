#!/usr/bin/env python
# coding: utf-8

# In[23]:


n = int(input())
t = [list(map(int, input().split())) for _ in range(n)]

#pb만들기
for i in range(1,n):
    for j in range(len(t[i])):
        # 양끝예외처리
        if j == 0:
            t[i][j] = t[i-1][0] + t[i][j]
        elif j == len(t[i])-1:
            t[i][j] = t[i-1][len(t[i])-2] + t[i][j]
        else:
            t[i][j] = max(t[i-1][j-1], t[i-1][j]) + t[i][j]
print(max(t[n-1]))


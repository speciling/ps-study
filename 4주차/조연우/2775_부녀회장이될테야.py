#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 아파트만들기
apt = [[i+1 for i in range(14)]]
for i in range(14):
    apt.append([0,]*14)   
for i in range(1,15):
    for j in range(14):
        if j==0:
            apt[i][j]=1
        else:
            apt[i][j] = apt[i-1][j]+apt[i][j-1]

# 정답출력
for tc in range(int(input())):
    k = int(input())
    n = int(input())
    print(apt[k][n-1])


# In[ ]:





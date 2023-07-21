#!/usr/bin/env python
# coding: utf-8

# In[7]:


n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

# 입력수만큼 pb만들기
if n>1:
    for i in range(1,n):
        rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
        rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
        rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]
print(min(rgb[-1]))


# In[ ]:





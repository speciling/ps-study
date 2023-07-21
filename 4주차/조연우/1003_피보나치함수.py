#!/usr/bin/env python
# coding: utf-8

# In[10]:


# pb만들기
pb = [[1,0], [0,1], ]
for _ in range(39):
    pb.append([0,0])
for i in range(2,41):
    pb[i][0] = pb[i-1][0]+pb[i-2][0]
    pb[i][1] = pb[i-1][1]+pb[i-2][1]

# 출력
for tc in range(int(input())):
    pm = int(input())
    print(*pb[pm])


# In[ ]:





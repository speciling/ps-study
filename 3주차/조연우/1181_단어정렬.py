#!/usr/bin/env python
# coding: utf-8

# In[10]:


n = int(input())

# 딕셔너리 계수정렬
dic={}

# set으로 중복제거
for i in range(51):
    dic[i] = set([])
for i in range(n):
    temp = input()
    dic[len(temp)].add(temp)

# list변환으로 정렬및출력
for i in range(51):
    if len(dic[i])>0:
        dic[i] = sorted(list(dic[i]))
        for j in range(len(dic[i])):
            print(dic[i][j])


# In[ ]:





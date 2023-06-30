#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 11047

n,k = map(int,input().split())
value = []
num = 0
for i in range(n):
    value.insert(0,int(input()))
for i in value:
    if k>=i:
        num += k//i
        k%=i
print(num)


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
time = map(int,input().split())
time = sorted(time)
sum = 0
for i in range(n):
    sum+=time[i]*(n-i)
print(sum)


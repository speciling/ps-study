#!/usr/bin/env python
# coding: utf-8

# In[23]:


n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
srt = sorted(a+b)
print(*srt)


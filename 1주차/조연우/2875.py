#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 2875

n,m,k = map(int,input().split())
team = 0
while(True):
    if n>=2 and m>=1 and m+n>=k+3:
        team += 1
        n -= 2
        m -= 1
    else:
        break
print(team)


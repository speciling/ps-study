#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num = list(input())
if '0' in num:
    if sum(map(int,num))%3==0:
        print(''.join(sorted(num, reverse=True)))
    else:
        print(-1)
else:
    print(-1)


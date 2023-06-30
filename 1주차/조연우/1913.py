#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num = int(input())
sc = []
for i in range(num):
    sc.append(list(map(int,input().split())))
sc.sort()
sc.sort(key=lambda x:x[1])
k = 0
count = 0
for i in range(num):
    if k <= sc[i][0]:
        count +=1
        k = sc[i][1]
print(count)


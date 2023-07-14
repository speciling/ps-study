#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n, m = map(int, input().split())
leng = [int(input()) for _ in range(n)]
start = 1
end = max(leng)
while(start <= end):
    total = 0
    mid = (start+end) // 2
    for x in leng:
        total += x//mid
    if total >= m:
        start = mid + 1
    else:
        end = mid -1
            
print(end)


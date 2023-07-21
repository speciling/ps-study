#!/usr/bin/env python
# coding: utf-8

# In[4]:


n = int(input())
s = [int(input()) for _ in range(n)]

# dp테이블만들기
# 계단이 1,2개인 경우
if n<3:
    print(sum(s))
# 아닌경우 점화식이용
else:
    dp = [0]*n
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    for i in range(2,n):
        dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
    print(dp[n-1])    


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 반복문으로 여러줄을 입력 받아야 할 때 시간초과 방지를 위해 sys.stdin.readline()을 사용
import sys
input = sys.stdin.readline

# 계수 정렬 이용
n = int(input())
num = [0]*10001
for _ in range(n):
    temp = int(input())
    num[temp] += 1
for i in range(10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i)


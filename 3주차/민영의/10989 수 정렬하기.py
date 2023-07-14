import sys
input = sys.stdin.readline
a = int(input())
ans = [0] * 10001
count = []
for _ in range(a):
    ans[int(input())] += 1
for i in range(len(ans)):
    for j in range(ans[i]):
        print(i)

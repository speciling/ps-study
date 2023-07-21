import sys
dp = [0, 0, 0]
for _ in range(int(input())):
    r, g, b = map(int, sys.stdin.readline().split())
    dp = [min(dp[1:])+r, min(dp[::2])+g, min(dp[:2])+b]
print(min(dp))
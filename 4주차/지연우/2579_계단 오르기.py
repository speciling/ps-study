import sys
dp = [0, [0, 0]]
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    dp = [max(dp[1]), [dp[0]+n, dp[1][0]+n]]
print(max(dp[1]))
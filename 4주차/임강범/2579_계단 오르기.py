n = int(input())
stairs = [int(input()) for _ in range(n)]

dp = [0]*(n)
dp[0] = stairs[0]
for i in range(1, n):
    if i == 1:
        dp[1] = stairs[0] + stairs[1]
    elif i == 2:
        dp[2] = max(stairs[0]+stairs[2],stairs[1]+stairs[2])
    else:    
        dp[i] = max(dp[i-2]+stairs[i],dp[i-3]+stairs[i-1]+stairs[i])
print(dp[i])
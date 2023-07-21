t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    dp = [[j+1 if i == 0 else 0 for j in range(n)]for i in range(k)]
    
    for i in range(1,k):
        for j in range(n):
            for m in range(j+1):
                dp[i][j] += dp[i-1][m]
    print(sum([ dp[k-1][j] for j in range(n)]))
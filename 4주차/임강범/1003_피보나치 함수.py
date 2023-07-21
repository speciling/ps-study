t = int(input())
result = []
for _ in range(t):
    n=int(input())
    dp =[[0]*2 for _ in range(n+1)]

    for i in range(0,n+1):
        if i == 0:
               dp[0][0] = 1
               dp[0][1] = 0
        elif i == 1:
            dp[1][0] = 0
            dp[1][1] = 1 
        else:
            dp[i][0] = dp[i-1][0]+dp[i-2][0]
            dp[i][1] = dp[i-1][1]+dp[i-2][1]
    
    result.append([dp[n][0],dp[n][1]])
for i in result:
    print(i[0],i[1])
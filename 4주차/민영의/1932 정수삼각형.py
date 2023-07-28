a = int(input())
p = [list(map(int, input().split())) for _ in range(a)]
for i in range(1, a):
    for j in range(i+1):
        if j == 0:
            p[i][j] += p[i-1][j]
        elif i == j:
            p[i][j] += p[i-1][j-1]
        else:
            p[i][j] = max(p[i][j] + p[i-1][j], p[i][j] + p[i-1][j-1])
print(max(p[a-1]))

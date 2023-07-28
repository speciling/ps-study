a = int(input())
p = [list(map(int, input().split())) for _ in range(a)]
for i in range(1, a):
    p[i][0] = p[i][0] + min(p[i-1][1], p[i-1][2])
    p[i][1] = p[i][1] + min(p[i-1][0], p[i-1][2])
    p[i][2] = p[i][2] + min(p[i-1][0], p[i-1][1])
print(min(p[a-1]))

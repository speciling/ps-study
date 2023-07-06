N, M, K = map(int, input().split())
t = 0
p = N + M
while N >= 2 and M >= 1:
    N -= 2
    M -= 1
    p -= 3
    if p < K:
        break
    t += 1
print(t)

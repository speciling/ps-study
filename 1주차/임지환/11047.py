N, K = map(int, input().split())
lst = []
count = 0
for i in range(N):
    lst.append(int(input()))
lst.reverse()
for i in range(N):
    count += K // lst[i]
    K -= lst[i] * (K // lst[i])
print(count)

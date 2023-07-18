n, t = map(int, input().split())
arr = list(map(int, input().split()))

s, e, ans = 0, 10**9, []
while s <= e:
    gap, cnt = (s+e)//2, 0
    tmp = arr[:]
    for i in range(n-1):
        if tmp[i+1] > tmp[i]+gap:
            cnt += tmp[i+1]-(tmp[i]+gap)
            tmp[i+1] = tmp[i]+gap
    for i in range(n-1, 0, -1):
        if tmp[i-1] > tmp[i]+gap:
            cnt += tmp[i-1]-(tmp[i]+gap)
            tmp[i-1] = tmp[i]+gap
    if cnt > t:
        s = gap+1
    else:
        ans = tmp
        e = gap-1
print(*ans)
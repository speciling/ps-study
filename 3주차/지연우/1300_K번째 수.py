n, k = int(input()), int(input())
s, e, ans = 1, n**2, 0
while s <= e:
    cnt, mid = 0, (s+e)//2
    for i in range(1, n+1):
        cnt += min(n, mid//i)
    if cnt < k:
        s = mid+1
    else:
        ans = mid
        e = mid-1
print(ans)
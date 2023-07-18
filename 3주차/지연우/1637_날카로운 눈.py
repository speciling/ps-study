import sys
arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(int(input()))]
s, e, ans = 0, 2**31, 0
while s <= e:
    m, cnt = (s+e)//2, 0
    for a, c, b in arr:
        if a <= m:
            cnt += (min(c, m)-a)//b + 1
    if cnt%2:
        ans = m
        e = m-1
    else:
        s = m+1

if ans:
    print(ans, sum((a<=ans<=c and not (ans-a)%b) for a, c, b in arr))
else:
    print("NOTHING")
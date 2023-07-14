n = int(input())
lst = []
cnt = 0
for _ in range(n):
    s, e = map(int,input().split())
    lst.append((s, e))
lst.sort(key=lambda x:x[0])
lst.sort(key=lambda x:x[1])
end = 0
for a, b in lst:
    if end <= a:
        end = b
        cnt +=1
print(cnt)

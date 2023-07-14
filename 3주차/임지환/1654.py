K, N = map(int,input().split())
lst = [int(input()) for __ in range(K)]

start = 1
end = max(lst)
result = 0
while (start<=end):
    mid = (start+end)//2
    total = 0
    for i in lst:
        total += i // mid
    if total < N:
        end = mid - 1
    else:
        result = mid
        start = mid +1
print(result)

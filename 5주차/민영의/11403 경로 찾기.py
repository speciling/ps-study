a = int(input())
arr = [list(map(int, input().split())) for _ in range(a)]
for i in range(a):
    for j in range(a):
        for k in range(a):
            if arr[j][i] == 1 and arr[i][k] == 1:
                arr[j][k] = 1
for l in arr:
    for m in l:
        print(m, end = ' ')
    print('')

import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
INF = int(1e9)
arr = [[INF for _ in range(a+1)] for _ in range(a+1)]

for _ in range(b):
    c, d, e = map(int, input().split())
    arr[c][d] = min(e, arr[c][d])
for i in range(1, a+1):
    arr[i][i] = 0
    for j in range(1, a+1):
        for k in range(1, a+1):
            if arr[j][k] > arr[j][i] + arr[i][k]:
                arr[j][k] = arr[j][i] + arr[i][k]
for i in range(1, a+1):
    for j in range(1, a+1):
        if arr[i][j] == INF:
            print(0, end = ' ')
        else:
            print(arr[i][j], end = ' ')
    print()

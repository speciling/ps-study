import sys
input = sys.stdin.readline
a, b = map(int, input().split())
line = []
for _ in range(a):
    line.append(int(input()))
start, end = 1, max(line)
while (start <= end):
    mid = (start + end) // 2
    total = 0
    for i in line:
        total += i // mid
    if total >= b:
        start = mid + 1
    else:
        end = mid - 1
print(end)

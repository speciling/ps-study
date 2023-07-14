import sys
input = sys.stdin.readline
count = []
num = input()
for i in range(len(num)):
    count.append(num[i])
for j in range(len(num)):
    for k in range(j, 0, -1):
        if count[k] > count[k-1]:
            count[k], count[k-1] = count[k-1], count[k]
        else:
            break
for ans in count:
    print(ans, end='')

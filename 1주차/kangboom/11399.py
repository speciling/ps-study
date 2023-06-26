N = int(input())

wait = list(map(int, input().split()))
wait.sort()

sum = 0
temp = 0

for t in wait:
    temp += t
    sum += temp 

print(sum)

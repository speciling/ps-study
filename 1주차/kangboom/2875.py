n, m, k = map(int, input().split())
count = 0

while(n >= 2 and m >= 1):
    n -= 2
    m -= 1
    count += 1

if n+m > k:
    print(count)
else:   
    num = k - (n+m)
    num1 = num // 3
    num2 = num % 3

    count -= num1
    if num2 != 0 :
        count -= 1

    print(count)

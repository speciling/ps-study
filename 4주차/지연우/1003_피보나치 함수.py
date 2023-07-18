dic = {0: (1, 0), 1: (0, 1)}

def fibo(n):
    global dic
    if n not in dic:
        a, b= fibo(n-1)
        c, d = fibo(n-2)
        dic[n] = (a+c, b+d)
    return dic[n]

for _ in range(int(input())):
    print(*fibo(int(input())))
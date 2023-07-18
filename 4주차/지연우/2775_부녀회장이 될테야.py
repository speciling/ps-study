for _ in range(int(input())):
    k, n = int(input()), int(input())
    arr = list(range(1, n+1))
    for i in range(k):
        arr = [sum(arr[:i]) for i in range(1, n+1)]
    print(arr[-1])
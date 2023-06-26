N, K = map(int, input().split())
value = [ int(input()) for _ in range(N)]

value.sort(reverse=True)

result = 0

for coin in value:
    result += K // coin
    K %= coin
     
print(result)

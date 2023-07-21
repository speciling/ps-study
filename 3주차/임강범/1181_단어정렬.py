n = int(input())
s = [ input() for _ in range(n)]
s = list(set(s))

s.sort
s.sort(key=lambda x : len(x))

for i in s:
    print(i)

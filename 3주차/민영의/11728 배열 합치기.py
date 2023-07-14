import sys
input = sys.stdin.readline
a = map(int, input().split())
b = list(map(int, input().split()))
c = list(map(int, input().split()))
b.extend(c)
print(*sorted(b))

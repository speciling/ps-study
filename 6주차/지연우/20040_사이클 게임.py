import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x, y = find(parent, x), find(parent, y)
    if x == y:
        return 1
    elif x < y:
        parent[y] = x
    else:
        parent[x] = y
    return 0

n, m = map(int, input().split())
p = list(range(n+1))
for i in range(m):
    a, b = map(int, input().split())
    if union(p, a, b):
        print(i+1)
        break
else:
    print(0)
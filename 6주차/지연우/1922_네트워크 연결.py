import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x, y = find(parent, x), find(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = int(input()), int(input())
p = list(range(n+1))
edges = sorted((tuple(map(int, input().split())) for _ in range(m)), key=lambda x:x[2])

ans = 0
for a, b, c in edges:
    if find(p, a) != find(p, b):
        union(p, a, b)
        ans += c
print(ans)
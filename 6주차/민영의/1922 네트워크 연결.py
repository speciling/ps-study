import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
parent = [0] * (a+1)
edges = []
result = 0
for i in range(1, a+1):
    parent[i] = i
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
def union_parent(c, d):
    c = find_parent(c)
    d = find_parent(d)
    if c < d:
        parent[d] = c
    else:
        parent[c] = d
for _ in range(b):
    e, f, cost = map(int, input().split())
    edges.append((cost, e, f))
edges.sort()
for j in edges:
    cost, e, f = j
    if find_parent(e) != find_parent(f):
        union_parent(e, f)
        result += cost
print(result)

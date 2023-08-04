import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
a, b = map(int, input().split())
parent = [0] * (a+1)
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
    e, f, g = map(int, input().split())
    if e == 0:
        union_parent(f, g)
    else:
        if find_parent(f) == find_parent(g):
            print('YES')
        else:
            print('NO')

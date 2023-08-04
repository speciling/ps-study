import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def union(parent, a, b):
    a, b = find(parent, a), find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

n, m = map(int, input().split())
p = list(range(n+1))
ans = []
for _ in range(m):
    o, a, b = map(int, input().split())
    if o:
        ans.append('YES' if find(p, a) == find(p, b) else 'NO')
    else:
        union(p, a, b)
print('\n'.join(ans))
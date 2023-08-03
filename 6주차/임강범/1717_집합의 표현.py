def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b :
        parent[b] = a
    else : 
        parent[b] = a

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
parent = [ i for i in range(n+1)]
result = []
for _ in range(m):
    x, y, z = map(int, input().split())
    cycle = False

    if x == 0:
        union_parent(parent, y, z)
    else:
        if find_parent(parent, y) == find_parent(parent, z):
            cycle = True

        if cycle:
            result.append("YES")
        else:
            result.append("NO")
print(*result, sep='\n')
        
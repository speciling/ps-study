def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

import sys
input = sys.stdin.readline

n = int(input())

parent = [i for i in range(n+1)]
graph = []
for _ in range(int(input())):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))

graph.sort()
result = 0
for i in graph:
    cost, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
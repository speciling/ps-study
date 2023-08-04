import sys
input = sys.stdin.readline
a, b = map(int, input().split())
parent = [i for i in range(a)]
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
def union_parent(c, d):
    c = find_parent(c)
    d = find_parent(d)
    if c == d:
        return True
    elif c < d:
        parent[d] = c
    else:
        parent[c] = d
    return False
answer = 0
for i in range(1, b+1):
    e, f = map(int, input().split())
    result = union_parent(e, f)
    if result and answer == 0:
        answer = i
print(answer)

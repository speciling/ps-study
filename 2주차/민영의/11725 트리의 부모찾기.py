import sys
sys.setrecursionlimit(10**6)
a = int(sys.stdin.readline())
tree = [[] for _ in range(a+1)]
visited = [0] * (a+1)
for i in range(a-1):
    num, com = map(int, input().split())
    tree[num].append(com)
    tree[com].append(num)
def dfs(i):
    for j in tree[i]:
        if not visited[j]:
            visited[j] = i
            dfs(j)
dfs(1)
for k in range(2, a+1):
    print(visited[k])

a = int(input())
b = int(input())
graph = [[],]
for _ in range(a):
    graph.append([])
for _ in range(b):
    num, com = map(int, input().split())
    for i in range(1, a+1):
        if i == num:
            graph[i].append(com)
        if i == com:
            graph[i].append(num)
virus = [0] * (a+1)
def dfs(graph,j, virus):
    virus[j] = 1
    for i in graph[j]:
        if not virus[i]:
            dfs(graph, i, virus)
dfs(graph, 1, virus)
virus[1] = 0
print(sum(virus))

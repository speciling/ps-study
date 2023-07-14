a = int(input())
graph = []
count = []
home = 0
for _ in range(a):
    graph.append(list(map(int, input())))
def dfs(x,y):
    global home
    if x <= -1 or x >= a or y >= a or y <= -1:
        return False
    if graph[x][y] == 1:
        home += 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False
result = 0
for i in range(a):
    for j in range(a):
        if dfs(i,j) == True:
            result += 1
            count.append(home)
            home = 0
print(result)
for k in sorted(count):
    print(k)

N = int(input())
val = [list(map(int,input().split())) for _ in range(N)]

val.sort(key=lambda x : x[0])
val.sort(key=lambda x : x[1])

result = 1
pre = val[0][1]
for i in range(1,N):

    if(val[i][0] >= pre):
        result+=1
        pre = val[i][1]
    
print(result)

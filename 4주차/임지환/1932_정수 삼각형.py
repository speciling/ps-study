import sys
input = sys.stdin.readline

N = int(input())
T = [list(map(int,input().split())) for _ in range(N)]

a = 2
for i in range(1,N): # 
    for j in range(a):
        if j == 0: # 첫 번째 열인 경우 아래 행 오른쪽과 더함
            T[i][j] = T[i][j] + T[i-1][j]
        elif i == j: # 마지막 열인 경우 아래 행 왼쪽과 더함
            T[i][j] = T[i][j] + T[i-1][j-1]
        else: # 둘 다 아닌 경우 아래 행 왼쪽열과 오른쪽 열 중 더 큰 값과 더함
            T[i][j] = max(T[i-1][j-1],T[i-1][j])+T[i][j]
    a += 1 # 아래 행으로 내려갈 수록 열도 하나씩 늘어나기 때문에 + 1
print(max(T[N-1])) # 마지막 행의 최댓값 출력

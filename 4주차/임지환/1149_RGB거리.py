import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

for i in range(1,N): # 색이 같지 않도록 최적화된 값 구하기
    lst[i][0] = min(lst[i-1][1], lst[i-1][2]) + lst[i][0] # 0번 인덱스와 같지 않게 1, 2번 인덱스 중 최솟값을 선택하여 0번 인덱스와 더함
    lst[i][1] = min(lst[i-1][0], lst[i-1][2]) + lst[i][1] # 1번 인덱스와 같지 않게 0, 2번 인덱스 중 최솟값을 선택하여 1번 인덱스와 더함
    lst[i][2] = min(lst[i-1][0], lst[i-1][1]) + lst[i][2] # 2번 인덱스와 같지 않게 0, 1번 인덱스 중 최솟값을 선택하여 2번 인덱스와 더함

print(min(lst[-1])) # 마지막 행에서 최솟값 출력

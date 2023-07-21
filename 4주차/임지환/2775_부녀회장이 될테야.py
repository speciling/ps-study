import sys
input = sys.stdin.readline

T = int(input())
a = 0

while a < T: # 테스트 케이스 만큼 반복
    k = int(input()) # 층 수 입력
    n = int(input()) # 호 수 입력
    lst = [i for i in range(1, n+1)] # 처음 호수 별 인원 리스트 생성

    for i in range(k):
        for j in range(1, n):
            lst[j] += lst[j-1] # k = 2 n = 3 을 입력했을 때 1 2 3 -> 1 3 6 -> 1 4 10

    result = lst[-1]
    print(result)
    a += 1

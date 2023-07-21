import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    f = [[]]*41  # N이 최대 40인 리스트 생성
    f[0] = [1, 0]  # 0번째 값 [1, 0]으로 초기화
    f[1] = [0, 1]  # 1번째 값 [0, 1]으로 초기화
    f[2] = [1, 1]  # 2번째 값 [1, 1]으로 초기화

    for i in range(3, N+1):  # 3부터 40까지 값 추가하기
        f[i] = [f[i-1][0]+f[i-2][0], f[i-1][1]+f[i-2][1]]  # 3부터 몇개 해보면 왼쪽의 식이 나옴

    print(f[N][0], f[N][1])

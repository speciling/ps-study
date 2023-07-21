import sys
input = sys.stdin.readline

T = int(input())
lst = [0 for i in range(301)] # 계단 별 점수 입력받을 리스트 생성
for i in range(T):
    lst[i] = int(input()) # 계단에 점수 입력

S = [0 for i in range(301)] # 계단의 누적된 점수를 받을 리스트 생성
S[0] = lst[0] # 첫 번째 계단 점수
S[1] = lst[0] + lst[1] # 두 번째 계단 점수
S[2] = max(lst[0]+lst[2], lst[1]+lst[2]) # 세 번째 계단 점수 = 두 칸 오르는 것과 한 칸씩 오르는 것 중 더 큰 값으로 초기화

for i in range(3,T):
    S[i] = max(lst[i]+lst[i-1]+s[i-3], S[i-2]+lst[i]) # 두칸 한칸 한칸 과 한칸 한칸 두칸 중 더 큰 값으로 선택

print(S[-1])

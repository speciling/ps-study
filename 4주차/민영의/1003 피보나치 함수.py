a = int(input())
num = [int(input()) for _ in range(a)]
ans1 = [1, 0]
ans2 = [0, 1]
for i in range(2, max(num)+1):
    ans1.append(ans1[i-1] + ans1[i-2])
    ans2.append(ans2[i-1] + ans2[i-2])
for j in num:
    print(ans1[j], ans2[j])

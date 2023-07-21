a = int(input())
score = [int(input()) for _ in range(a)]
score.insert(0, 0)
new = [*score]
for i in range(2, a+1):
    score[i] += max(score[i-2], new[i-2])
    new[i] += score[i-1]
print(max(score[a], new[a]))

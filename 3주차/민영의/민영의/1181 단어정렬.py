a = int(input())
word = []
for _ in range(a):
    b = input()
    word.append(b)
word = sorted(set(word), key = lambda x:(len(x), x))
for i in word:
    print(i)

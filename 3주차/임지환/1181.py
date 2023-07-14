n = int(input())
lst = []
for i in range(n):
    a = input()
    lst.append(a)
lst = set(lst)
dic = {}
for j in lst:
    dic[j] = len(j)
dic = sorted(dic)
dic.sort(key = len)
for k in range(len(dic)):
    print(dic[k])

a = list(input())
a.sort(reverse=True)
num = 0
result=int("".join(a))
for i in a:
    num+=int(i)
if num % 3!=0 or int(result) % 10 !=0:
    result=-1
print(result)

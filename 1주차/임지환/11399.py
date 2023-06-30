a = int(input())
lst = [int(num) for num in input().split()]
lst.sort()
c = 0
for i in range(len(lst)):
    c += sum(lst[0:i+1])
print(c)

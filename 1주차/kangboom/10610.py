n = input()

val = [int(i) for i in n]
val.sort(reverse=True)

sum = 0
if(val[-1] != 0):
    print("-1")
else:
    for i in val:
        sum += i

if(sum % 3 == 0):
    print(''.join(str(_) for _ in val))
else:
    print("-1")
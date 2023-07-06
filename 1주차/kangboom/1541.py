n = input()

if(n.find("-") != -1):
    s = (n.split("-",1))
    print(sum(map(int,s[0].split("+")))-sum(map(int,s[1].replace('-','+').split('+'))))
else:
    print(sum(map(int,n.split("+"))))

n = int(input())
num = 1 

for i in range(1,n+1):
    if i==1:
        s = ""
        for j in range(1,n+1):
            s += str(num)+" "
            num += 1
        num -= 1
        print(s)
    elif i == n:
        print(num+1)
    else:
        print(str(num+1)+" " + "  "*(n-i-1) + str(num+n-i+1))
        num += n-i+1
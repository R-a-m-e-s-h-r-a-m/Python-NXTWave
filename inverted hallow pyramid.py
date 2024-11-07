n = int(input())
s = int(input())
for i in range(1,n+1):
    if i==n:
        print(" "*(i-1) + str(s))
    elif i==1:
        row = ""
        for j in range(s,s+n):
            row += str(j) + " "
        print(row)
    else:
        print(" "*(i-1) + str(s)+" " + "  "*(n-i-1) + str(s+n-i))
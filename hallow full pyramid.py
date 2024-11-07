n= int(input())
for i in range(1,n+1):
    if i==n:
        for j in range(1,n+1):
            print(j,end=" ")
    elif i==1:
        print(" "*(n-i) + "1")
    else:
        print(" "*(n-i) + "1 " + " "*(2*i-4) + str(i))
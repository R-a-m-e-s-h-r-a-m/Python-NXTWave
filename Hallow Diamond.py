n = int(input())
for i in range(1,n+1):
    if i==1:
        print(" "*(n-i) + "*")
    else:
        print(" "*(n-i) + "*" + " "*(2*i-3) + "*")
for i in range(1,n):
    if i==n-1:
        print(" "*i + "*")
    else:
        print(" "*i + "*" + " "*(2*(n-i-1)-1) + "*")
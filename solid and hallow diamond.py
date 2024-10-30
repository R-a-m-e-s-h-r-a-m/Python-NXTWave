n = int(input())
for i in range(1,n+1):
    print(" "*(n-i) + "* "*i)
for i in range(1,n):
    if i == n-1:
        print(" "*i + "*")
    else:
        print(" "*i + "*" + " "*(2*(n-i)-3) + "*")
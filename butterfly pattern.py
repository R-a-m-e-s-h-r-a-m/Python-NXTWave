n = int(input())
for i in range(1,n+1):
    print("* "*i + " "*4*(n-i) + "* "*i)
for i in range(1,n):
    print("* "*(n-i) + " "*4*i + "* "*(n-i))
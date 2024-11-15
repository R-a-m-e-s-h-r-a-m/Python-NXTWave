n = int(input())
for i in range(n):
    if i == 0:
        print(" "*(n-i-1) + "/\\")
    else:
        print(" "*(n-i-1) + "/" + " "*(2*i) + "\\")
        
for i in range(n,0,-1):
    if i == 1:
        print(" "*(n-i) + "\\/")
    else:
        print(" "*(n-i) + "\\" + " "*(2*i-2) + "/")
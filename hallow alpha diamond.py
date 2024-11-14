n = int(input())
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1,n+1):
    if i==1:
        print(" "*(n-i) + "A")
    else:
        print(" "*(n-i) + chars[i-1] + " "*(2*i-3) + chars[i-1])
        
for i in range(n-1,0,-1):
    if i==1:
        print(" "*(n-i) + "A")
    else:
        print(" "*(n-i) + chars[i-1] + " "*(2*i-3) + chars[i-1])
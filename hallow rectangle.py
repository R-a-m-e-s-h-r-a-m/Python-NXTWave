m = int(input())
n = int(input())
prod = m*n 
for i in range(1,m+1):
    for j in range(1,n+1):
        if i==1 or i==m or j==1 or j==n:
            print(prod,end=" ")
        else:
            print("  ",end="")
        prod -= 1
    print()
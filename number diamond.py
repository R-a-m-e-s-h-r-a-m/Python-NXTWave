n = int(input())

for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
        
for i in range(1,n):
    print(" "*i,end="")
    for j in range(1,n-i+1):
        print(j,end=" ")
    print()
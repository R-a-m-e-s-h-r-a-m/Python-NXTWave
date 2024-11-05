n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i

for i in range(n,0,-1):
    print("  "*(n-i),end="")
    for j in range(i):
        print(sum,end=" ")
        sum -= 1 
    print()
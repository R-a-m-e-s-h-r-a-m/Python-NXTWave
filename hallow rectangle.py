a = int(input())
b = int(input())
sum = 1
for i in range(1,a+1):
    for j in range(1,b+1):
        if i==1 or i==a or j==1 or j==b:
            print(sum,end=" ")
            
        else:
            print(" ",end=" ")
        sum += 1
    print()
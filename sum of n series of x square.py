x = int(input())
n = int(input())

sum = 0
for i in range(1,n+1):
    sum += pow(int(str(x)*i),2)
print(sum)
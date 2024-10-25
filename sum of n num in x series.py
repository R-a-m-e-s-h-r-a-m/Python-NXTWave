x = int(input())
n = int(input())
sum = 0
for i in range(1,n+1):
    sum += int(str(x)*i)
print(sum)
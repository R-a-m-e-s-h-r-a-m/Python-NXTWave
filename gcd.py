m = int(input())
n = int(input())
while n:
    m,n = n,m%n 
print(m)
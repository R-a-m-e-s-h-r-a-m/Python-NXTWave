n = int(input())
k = int(input())
for i in range(n):
    if n%(n-i) == 0:
        k -= 1 
        if k==0:
            print(n-i)
            break
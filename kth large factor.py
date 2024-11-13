n = int(input())
k = int(input())
count = 0
for i in range(n,0,-1):
    if n%i == 0:
        count += 1
        if k == count:
            print(i)
            break
else:
    print("1")
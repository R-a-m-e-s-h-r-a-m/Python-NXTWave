n = int(input())
for i in range(n):
    num = int(input())
    count = 0
    for i in range(2,num):
        if num%i == 0:
            count += 1
            break
    if count == 0 and num > 1:
        print(num)
        break
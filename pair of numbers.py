a = int(input())
count = 0
for i in range(1,a+1):
    for j in range(1,a+1):
        if i<j and (i+j == a):
            count += 1
print(count)
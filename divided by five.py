n = int(input())
L = []
for i in range(n):
    num = int(input())
    if num % 5 == 0:
        L += [num]
print(L)
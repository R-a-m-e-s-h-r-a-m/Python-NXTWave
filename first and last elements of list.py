n = int(input())
L,L1 = [],[]
for i in range(n):
    num = int(input())
    L += [num]
for i in range(len(L)):
    if i<2 or i>=(n-2):
        L1 += [L[i]]
print(L1)
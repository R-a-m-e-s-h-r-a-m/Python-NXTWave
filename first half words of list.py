s = input()
l1 = s.split()
if len(l1)%2 == 0:
    n = len(l1)//2
else:
    n = len(l1)//2 + 1
print(l1[:n])
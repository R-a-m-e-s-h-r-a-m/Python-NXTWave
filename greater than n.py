num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]
# Write your code here
num = int(input())
L = []
for i in num_list:
    if i > num:
        L += [i]

print(L)
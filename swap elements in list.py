L = [1, "two", 9, 5.09, "Three", -558, "four", -93.7, "six"]

#Write your code here
a = int(input())
b = int(input())

temp = L[a]
L[a] = L[b]
L[b] = temp
print(L)
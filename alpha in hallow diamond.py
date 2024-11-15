n = int(input())
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum = 1
for i  in range(n):
    if i == 0:
        print(" "*(n-i-1) + "A")
    else:
        print(" "*(n-i-1) + chars[sum]+ " "*(2*i-1) + chars[sum+1])
        sum += 2

sum -= 4  

for i  in range(n-1,0,-1):
    if i == 1:
        print(" "*(n-i) + "A")
    else:
        print(" "*(n-i) + chars[sum]+ " "*(2*(i-1)-1) + chars[sum+1])
        sum -= 2
n = int(input())
col = 2*n - 1
for i in range(n):
    dots = ". "*(n-i-1)
    zeroes = "0 "*(2*i+1)
    print(dots + zeroes + dots)
    
for i in range(n-1,0,-1):
    dots = ". "*(n-i)
    zeroes = "0 "*(2*i-1)
    print(dots + zeroes + dots)
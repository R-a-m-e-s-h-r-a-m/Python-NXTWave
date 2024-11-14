n = int(input())
for i in range(n):
    stars = "* "*(n-i)
    spaces = "  "*(2*i)
    print(stars + spaces + stars)
for i in range(n,0,-1):
    stars = "* "*(n-i+1)
    spaces = "  "*(2*i-2)
    print(stars + spaces + stars)
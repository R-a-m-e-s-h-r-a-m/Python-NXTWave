s = int(input())
n = int(input())



for i in range(1,n+1):
    if i==1:
        first_row = ""
        for j in range(1,n+1):
            first_row += str(s) + " "
            s += 1
        print(first_row)
    elif i == n:
        print(" "*(i-1) + str(s))
    else:
        middle_row = ""
        first_space = " "*(i-1)
        middle_row += first_space + str(s) + " "
        s += n-i
        hallow_space = "  "*(n-i-1)
        middle_row += hallow_space + str(s)
        s += 1
        print(middle_row)
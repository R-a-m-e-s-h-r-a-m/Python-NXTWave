n = int(input())
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
    spaces = " "*(n-i-1)
    mid_spaces = " "*(2*i-1)
    if i == 0:
        print(spaces + chars[i] + 2*spaces+" " + chars[i])
    else:
        print(spaces + chars[i] + mid_spaces + chars[i] + 2*spaces+" " + chars[i] + mid_spaces + chars[i])
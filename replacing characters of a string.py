s = input()
for i in s:
    if i == " ":
        print(" ",end="")
    else:
        print(chr(ord(i)+1),end="")
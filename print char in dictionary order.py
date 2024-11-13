s = input()
small,large = ord(s[0]),ord(s[0])
for i in s:
    if ord(i)<small:
        small = ord(i)
    elif ord(i)>large:
        large = ord(i)
print(chr(small) + " " + chr(large))
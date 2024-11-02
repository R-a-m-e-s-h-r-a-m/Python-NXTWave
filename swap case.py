s = input()
s2 = ""
for i in s:
    if i.isupper():
        s2 += i.lower()
    else:
        s2 += i.upper()
print(s2)
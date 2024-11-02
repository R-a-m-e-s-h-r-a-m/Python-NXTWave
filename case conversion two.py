s = input()
s2 = ""
for i in range(len(s)):
    if s[i] == s[i].upper():
        s2 += "-"+s[i].lower()
    else:
        s2 += s[i]
print(s2)
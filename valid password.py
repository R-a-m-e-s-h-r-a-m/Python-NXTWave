s = input()
upper_count = 0
lower_count = 0
digit_count = 0

for i in s:
    if i.isupper():
        upper_count += 1 
    elif i.islower():
        lower_count += 1 
    elif i.isdigit():
        digit_count += 1 
        
if upper_count>0 and lower_count>0 and digit_count>0:
    print("Valid Password")
else:
    print("Invalid Password")
full_string = input()
sub_string = input()
sub_string_index = 0
sub_string_len = len(sub_string)

for i in full_string:
    if i == sub_string[sub_string_index]:
        sub_string_index += 1 
        if sub_string_index == sub_string_len:
            break 
if sub_string_index == sub_string_len:
    print("Yes")
else:
    print("No")
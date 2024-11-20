def get_lower_and_upper_case_letters(word):
    lower_letters,upper_letters = "",""
    for i in word:
        if i.islower():
            lower_letters += i 
        else:
            upper_letters += i 
    print(upper_letters+"\n"+lower_letters)


word = input()
get_lower_and_upper_case_letters(word)
def number_of_cars_needed(no_of_people):
    total = 0
    total += no_of_people//5
    rem = no_of_people%5
    if rem == 0:
        print(total)
    else:
        print(total+1)


no_of_people = int(input())
number_of_cars_needed(no_of_people)
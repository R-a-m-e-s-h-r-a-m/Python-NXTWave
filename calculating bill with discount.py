def calculate_bill(amount):
    # Complete this function
    if amount<500:
        amount = amount - (5/100)*amount
        print(amount)
    elif amount>=500 and amount<2500:
        amount = amount - (10/100)*amount
        print(amount)
    else:
        amount = amount - (20/100)*amount
        print(amount)


amount = int(input())
# Call the calculate_bill function
calculate_bill(amount)
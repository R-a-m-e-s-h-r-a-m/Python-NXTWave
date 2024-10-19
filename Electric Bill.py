a = int(input())

if a<=50:
    bill = (a*2)
    print(bill + bill*0.2)
elif a<=150:
    bill = ((50*2) + (a-50)*3)
    print(bill + bill * 0.2)
elif a<=250:
    bill = ((50*2) + (100*3) + (a-150)*5)
    print(bill + bill* 0.2)
elif a>250:
    bill = ((50*2) + (100*3) + 100*5 + (a-250)*8)
    print(bill + bill * 0.2)
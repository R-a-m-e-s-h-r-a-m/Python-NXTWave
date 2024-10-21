a = int(input())

if a>0 and a<=40:
    print(a*2 + 50)
elif a>40 and a<=60:
    print(40*2 + (a-40)*4 + 50)
elif a>60 and a<=120:
    print(40*2 + 20*4 + (a-60)*6 + 50)
elif a>120:
    print(40*2 + 20*4 + 60*6 + (a-120)*8 + 50)
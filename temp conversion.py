t = input()
degree = t[-1]
t = float(t[:-1])

if degree == "F":
    c = (t - 32) * 5 / 9
    print(str(round(c,2)) + "C")
    print(str(round(t,1)) + "F")
    k = c + 273
    print(str(round(k,2)) + "K")
elif degree == "K":
    c = t - 273
    print(str(round(c,1)) + "C")
    f = ((9*c) / 5) + 32
    print(str(round(f,1)) + "F")
    print(str(round(t,1)) + "K")
else:
    print(str(round(t,1)) + "C")
    f = ((9*t) / 5) + 32
    print(str(round(f,1)) + "F")
    k = t + 273
    print(str(round(k,1)) + "K")
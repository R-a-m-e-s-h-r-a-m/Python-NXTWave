n = int(input())
count = 0
for i in range(2,10):
    if n % i == 0:
        count += 1
if count == 0:
    print("Indivisible Number")
else:
    print("Divisible Number")
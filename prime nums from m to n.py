def check_is_prime(m, n):
    prime_nums = ""
    for i in range(m,n+1):
        count = 0
        for j in range(2,i):
            if i%j == 0:
                count += 1 
                break
        if count == 0 and i!=1 and i!=0:
            prime_nums += str(i)+" " 
    return prime_nums
m = int(input())
n = int(input())

prime_numbers =    check_is_prime(m,n)

print(prime_numbers)
def sum_of_cubes_m_to_n(m, n):
    sum = 0
    for i in range(m,n+1):
        sum += pow(i,3)
    print(sum)


m = int(input())
n = int(input())
sum_of_cubes_m_to_n(m,n)
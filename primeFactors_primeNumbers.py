def factors(n):
    factorlist = []
    k = 2
    while k <= n:
        while n % k == 0:
            factorlist.append(k)
            n //= k
        k += 1
    return factorlist


for n in range(3, 100):
    if len(factors(n)) == 1:
        print(n)

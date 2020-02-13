def factorial(n):
    f = 1
    for k in range(1, n + 1):
        f *= k
    return f


def binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def PascalTri(x):
    for n in range(x):
        k = 0
        b = []
        while k <= n + 1:
            b.append(binomial(n, k))
            k += 1
    return b


y = int(input("Pick your Pascal Triangle nth Number :"))
for i in range(y+1):
    if i == 0:
        print(0)
        print([1])
    else:
        print(i)
        print(PascalTri(i))

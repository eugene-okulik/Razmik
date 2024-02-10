import gmpy2


def fib_rec():
    a, b = gmpy2.mpz(1), gmpy2.mpz(1)
    while True:
        yield a
        a, b = b, a + b


for index, i in enumerate(fib_rec()):
    if index in [4, 99, 999, 99999]:
        print(i)

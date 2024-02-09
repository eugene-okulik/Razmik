import gmpy2


def fib_rec(length):
    a, b = gmpy2.mpz(1), gmpy2.mpz(1)
    for i in range(length):
        yield a
        a, b = b, a + b


list_fibonaci = list(fib_rec(100000))
print(list_fibonaci[4], list_fibonaci[99], list_fibonaci[999], list_fibonaci[99999])

import gmpy2


def fib_rec():
    a, b = gmpy2.mpz(1), gmpy2.mpz(1)
    while True:
        yield a
        a, b = b, a + b


desired_numbers = [4, 99, 999, 99999]

for index, i in enumerate(fib_rec()):
    if index in desired_numbers:
        print(i)
    if index == max(desired_numbers):
        break

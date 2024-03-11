import math
from time import time as t

def is_prime(n):
    if n == 1 or n == 0:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for d in range(5, math.isqrt(n)+1, 6):
        if d % 11**6 == 0:
            print(d)
        if n % d == 0 or n % (d + 2) == 0:
            return False
    return True

s = t()

print(is_prime(1_000_000_007))

print((t() - s) * 250_000)

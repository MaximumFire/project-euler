from math import prod
from itertools import combinations, permutations

def is_cyclic(x):
    n = len(x)
    for i in range(n):
        if str(x[i])[2:] != str(x[(i+1)%n])[:2]:
            return False
    return True

def check(x):
    return any([is_cyclic(y) for y in permutations(x)])

def semi_check(x):
    r = 0
    c = list(combinations([n for n in range(len(x))], 2))
    for a in c:
        if str(x[a[0]])[2:] == str(x[a[1]])[:2] or str(x[a[1]])[2:] == str(x[a[0]])[:2]:
            r += 1
    if r < (len(x) - 1):
        return False
    return True

triangles = [(n*(n+1))//2 for n in range(1, 142) if 10000 > (n*(n+1))//2 >= 1000][::-1]
squares = [(n**2) for n in range(1, 102) if 10000 > (n**2) > 1000][::-1]
pentagons = [(n*(3*n-1))//2 for n in range(1, 83) if 10000 > (n*(3*n-1))//2 >= 1000]
hexagons = [(n*(2*n-1)) for n in range(1, 72) if 10000 > (n*(2*n-1)) >= 1000][::-1]
heptagons = [(n*(5*n-3))//2 for n in range(1, 65) if 10000 > (n*(5*n-3))//2 >= 1000]
octagons = [(n*(3*n-2)) for n in range(1, 60) if 10000 > (n*(3*n-2)) >= 1000]

for a in triangles:
    for b in squares:
        if not semi_check((a, b)):
            continue
        for c in pentagons:
            if not semi_check((a, b, c)):
                continue
            for d in hexagons:
                if not semi_check((a, b, c, d)):
                    continue
                for e in heptagons:
                    if not semi_check((a, b, c, d, e)):
                        continue
                    for f in octagons:
                        if check((a, b, c, d, e, f)):
                            print((a, b, c, d, e, f), sum((a, b, c, d, e, f)))
                            exit(0)
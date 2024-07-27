from math import prod

def is_cyclic(x):
    n = len(x)
    for i in range(n):
        if str(x[i])[2:] != str(x[(i+1)%n])[:2]:
            return False
    return True

triangles = [(n*(n+1))//2 for n in range(1, 142) if 10000 > (n*(n+1))//2 >= 1000]
squares = [(n**2) for n in range(1, 102) if 10000 > (n**2) > 1000]
pentagons = [(n*(3*n-1))//2 for n in range(1, 83) if 10000 > (n*(3*n-1))//2 >= 1000]
hexagons = [(n*(2*n-1)) for n in range(1, 72) if 10000 > (n*(2*n-1)) >= 1000]
heptagons = [(n*(5*n-3))//2 for n in range(1, 65) if 10000 > (n*(5*n-3))//2 >= 1000]
octagons = [(n*(3*n-2)) for n in range(1, 60) if 10000 > (n*(3*n-2)) >= 1000]

print(prod([len(triangles), len(squares), len(pentagons), len(hexagons), len(heptagons), len(octagons)]))

for a in triangles:
    for b in squares:
        for c in pentagons:
            for d in hexagons:
                for e in heptagons:
                    for f in octagons:
                        if is_cyclic((a, b, c, d, e, f)):
                            print((a, b, c, d, e, f), sum((a, b, c, d, e, f)))
                            exit(0)
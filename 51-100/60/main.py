from sympy import isprime
import json
from itertools import combinations

cache = {}

def check_combination(combo):
    if combo not in cache:
        cache[combo] = isprime(int(f"{combo[0]}{combo[1]}")) and isprime(int(f"{combo[1]}{combo[0]}"))
    return cache[combo]

def check(combo):
    if all([check_combination(c) for c in combinations(combo, 2)]):
        return True
    return False

with open("C:/Users/conno/Onedrive/Documents/Github/project-euler/primes_million.json", "r+") as f:
    primes = json.loads(f.read())["primes"][:1100]

for a in primes:
    for b in primes[primes.index(a)+1:]:
        if not check((a, b)):
            continue
        for c in primes[primes.index(b)+1:]:
            if not check((a, b, c)):
                continue
            for d in primes[primes.index(c)+1:]:
                if not check((a, b, c, d)):
                    continue
                for e in primes[primes.index(d)+1:]:
                    if check((a, b, c, d, e)):
                        print((a, b, c, d, e), sum((a, b, c, d, e)))
                        exit(0)
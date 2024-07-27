import json
import numpy as np
from numba import jit, njit

with open("C:/Users/conno/Onedrive/Documents/Github/project-euler/primes_million.json", "r+") as f:
    primes = json.loads(f.read())["primes"]
    

@njit
def concatenate_ints(a, b):
    def count_digits(n):
        count = 0
        while n != 0:
            n //= 10
            count += 1
        return count
    
    return a * (10 ** count_digits(b)) + b


@jit(nopython=True)
def check_sums(args):
    if len(args) == 0 or len(args) == 1:
        return False
    for i in range(len(args)):
        for j in range(i+1, len(args)):
            s1 = concatenate_ints(args[i], args[j])
            s2 = concatenate_ints(args[j], args[i])
            if s1 not in primes_set or s2 not in primes_set:
                return False
    return True

@jit(nopython=True)
def main():
    for a in range(0, len(primes)):
        print(f"a: {primes[a]}")
        for b in range(a, len(primes)):
            print(f"b: {primes[b]}")
            if not check_sums(np.array([primes[a], primes[b]])):
                continue
            for c in range(b, len(primes)):
                if not check_sums(np.array([primes[a], primes[b], primes[c]])):
                    continue
                for d in range(c, len(primes)):
                    if not check_sums(np.array([primes[a], primes[b], primes[c], primes[d]])):
                        continue
                    for e in range(d, len(primes)):
                        if check_sums(np.array([primes[a], primes[b], primes[c], primes[d], primes[e]])):
                            print(primes[a], primes[b], primes[c], primes[d], primes[e], sum([primes[a], primes[b], primes[c], primes[d], primes[e]]))
                            return

main()
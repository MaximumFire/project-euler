import json
from sympy import isprime, prime
from itertools import combinations
import multiprocessing as mp
import numpy as np

def check_combination(combo):
    return isprime(int(f"{combo[0]}{combo[1]}")) and isprime(int(f"{combo[1]}{combo[0]}"))

def carry_out_checks_on_combos(combos):
    for combo in combos:
        if all([check_combination(c) for c in combinations(combo, 2)]):
            print(combo, sum(list(combo)))
            return combo, sum(list(combo))
    return None

def chunks(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

if __name__ == "__main__":  
    with open("C:/Users/conno/Onedrive/Documents/Github/project-euler/primes_10_million.json", "r+") as f:
        primes = np.array(json.loads(f.read())["primes"][:1000], dtype=np.int32)
    prime_combinations = combinations(primes, 5)
    
    with mp.Pool(processes=mp.cpu_count()) as pool:
        results = pool.map(carry_out_checks_on_combos, prime_combinations)

    for r in results:
        if r:
            print(r)
    
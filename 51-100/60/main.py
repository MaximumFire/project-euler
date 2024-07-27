import json
from sympy import isprime, prime
from itertools import combinations
import multiprocessing as mp
import numpy as np

def check_combination(combo):
    return isprime(int(f"{combo[0]}{combo[1]}")) and isprime(int(f"{combo[1]}{combo[0]}"))

def carry_out_checks_on_combos(combos, output_queue):
    for combo in combos:
        if all([check_combination(c) for c in combinations(combo, 2)]):
            print(combo, sum(list(combo)), flush=True)
            output_queue.put((combo, sum(list(combo))))
    output_queue.put(None)

def chunks(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

if __name__ == "__main__":  
    n_proc = 12
    with open("C:/Users/conno/Onedrive/Documents/Github/project-euler/primes_10_million.json", "r+") as f:
        primes = np.array(json.loads(f.read())["primes"][:170], dtype=np.int32)
    prime_combinations = list(combinations(primes, 5))
    chunked_combinations = list(chunks(prime_combinations, int(sum(1 for c in prime_combinations) / n_proc)+1))
    processes = []
    output_queue = mp.Queue()
    results = []

    for chunk in chunked_combinations:
        process = mp.Process(target=carry_out_checks_on_combos, args=(chunk, output_queue,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    while not output_queue.empty():
        results.append(output_queue.get())

    for r in results:
        if r:
            print(r)
    
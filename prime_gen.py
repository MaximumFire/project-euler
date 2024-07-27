import json

def primes(n):
    prime = [1 for i in range(n+1)]
    p = 2
    while(p * p <= n):
        if (prime[p] == 1):
            for i in range(p * p, n + 1, p):
                prime[i] = 0
        p += 1
    return prime

with open("c:/Users/conno/Onedrive/Documents/Github/project-euler/primes_billion.json", "w+") as f:
    f.write(json.dumps({"primes": primes(1000_000_000)}))


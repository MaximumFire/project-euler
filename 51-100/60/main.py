import json
from tabnanny import check

with open("C:/Users/conno/Onedrive/Documents/Github/project-euler/primes_million.json", "r+") as f:
    primes = json.loads(f.read())["primes"][:100000]
    primes_set = set(primes)

def check_sums(*args):
    sums = [
        str(args[0]) + str(args[1]),
        str(args[0]) + str(args[2]),
        str(args[0]) + str(args[3]),
        # str(args[0]) + str(args[4]),
        str(args[1]) + str(args[2]),
        str(args[1]) + str(args[3]),
        # str(args[1]) + str(args[4]),
        str(args[2]) + str(args[3]),
        # str(args[2]) + str(args[4]),
        # str(args[3]) + str(args[4])
    ]
    for s in sums:
        if int(s) not in primes_set:
            return False
    return True

for a in range(0, len(primes)):
    # add extra checks here, obviously if a = 0, b = 0, 22 is going to be in the sums which wont work
    for b in range(a, len(primes)):
        for c in range(b, len(primes)):
            print(a, b, c)
            for d in range(c, len(primes)):
                sums = [
                    str(primes[a]) + str(primes[b]),
                    str(primes[a]) + str(primes[c]),
                    str(primes[a]) + str(primes[d]),
                    # str(primes[a]) + str(primes[e]),
                    str(primes[b]) + str(primes[c]),
                    str(primes[b]) + str(primes[d]),
                    # str(primes[b]) + str(primes[e]),
                    str(primes[c]) + str(primes[d]),
                    # str(primes[c]) + str(primes[e]),
                    # str(primes[d]) + str(primes[e])
                ]
                
                if check_sums(primes[a], primes[b], primes[c], primes[d]):
                    print(a, b, c, d)
                    exit(0)
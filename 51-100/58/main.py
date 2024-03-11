"""
43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31

1, 3, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49

(9 - 6) + (9 - 4) + (9 - 2) + 9
(25 - 12) + (25 - 8) + (25 - 4) + 25
(49 - 18) + (49 - 12) + (49 - 6) + 49

n**2, (n**2)-(1*(n-1)), (n**2)-(2*(n-1)), (n**2)-(3*(n-1))

"""
import json

with open("C:/Users/conno/Onedrive/Documents/Github/project-euler/primes_billion.json", "r+") as f:
    primes = json.loads(f.read())["primes"]

primes_set = set(primes)

total = 1
total_prime = 0
x = 100
n = 3
while True:
    total += 4
    for i in range(0, 4):
        if (n**2)-(i*(n-1)) in primes_set:
            total_prime += 1
            print((n**2)-(i*(n-1)))
    x = (total_prime / total) * 100
    if x < 10:
        print(n, x)
        a = input()
        exit(0)
    if (n**2) > 999_999_999:
        exit(1)
    n += 2
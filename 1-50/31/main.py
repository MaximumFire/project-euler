ways = [(1 if i == 0 else 0) for i in range(201)]
for x in [1, 2, 5, 10, 20, 50, 100, 200]:
    for i in range(x, 201):
        ways[i] += ways[i-x]
print(ways[200])
sum = 1
"""
43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31

1, 3, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49

1 
+ 4(9) - 3(3) - 3
+ 4(25) - 3(5) - 9
+ 4(49) - 3(7) - 15

3:1
5:3
7:5


"""

total = 1
for i in range(3, 1002, 2):
    total = total + 4*(i**2) - 3*(i) - 3*(i - 2)
print(total)

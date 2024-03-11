from string import ascii_lowercase

letters = [ord(x) for x in list(ascii_lowercase)]

with open("C:/Users/conno/Onedrive/Documents/Github/project-euler/51-100/59/cipher.txt") as f:
    s = [int(x) for x in f.read().split(",")]

for i in range(0, 26):
    for j in range(0, 26):
        for k in range(0, 26):
            key = [letters[i], letters[j], letters[k]]
            x = 0
            y = 0
            
            
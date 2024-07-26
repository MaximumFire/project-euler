alphabet = [x for x in range(97, 123)]

with open("C:/Users/conno/Onedrive/Documents/Github/project-euler/51-100/59/cipher.txt", "r+") as f:
    encrypted_letters = [int(x) for x in f.readline().split(",")]

for x in alphabet:
    for y in alphabet:
        for z in alphabet:
            curr_key = (x, y, z)
            curr_i = 0
            curr_str = ""
            for w in encrypted_letters:
                curr_str += chr(w ^ curr_key[curr_i % 3])
                curr_i += 1
            if " the " in curr_str:
                print(curr_str, "\n", curr_key)
                print(sum([ord(w) for w in curr_str]))
                exit(0)
                
word = input()

wordlist = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for a in wordlist:
    word = word.replace(a, "*")

print(len(word))
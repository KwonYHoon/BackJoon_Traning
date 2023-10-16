# 크로아티아 (핵심 : replace)

croatia = ["c=", 'c-', "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()

for i in croatia:
    word = word.replace(i, "*")

print(len(word))
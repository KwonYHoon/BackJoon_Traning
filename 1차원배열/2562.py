Array = []

for i in range(9):
    Array.append(int(input()))

print(max(Array))
print(Array.index(max(Array)) + 1)
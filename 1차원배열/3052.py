Array = []

for i in range(1, 10 + 1) :
    Array.append(int(input()) % 42)

print(len(set(Array)))
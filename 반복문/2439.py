Star = int(input())

for i in range(Star):
    for j in range(Star - (i + 1)):
        print(" ", end = "")
    for a in range(i + 1):
        print("*", end = "")
    
    print()
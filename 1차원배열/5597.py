Array = [0] * (30 + 1)

for i in range(1, 28 + 1) :
    n = int(input())
    Array[n] += 1

for i in range(1, len(Array)) :
    if(Array[i] == 0) :
        print(i)
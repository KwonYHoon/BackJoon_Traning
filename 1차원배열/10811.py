N,M = map(int, input().split())

Array = [i for i in range(1, N + 1)]

for i in range(M) :
    i, j = map(int, input().split())
    temp = Array[i - 1 : j]
    temp.reverse()
    Array[i - 1 : j] = temp

for i in range(N) :
    print(Array[i], end = " ")
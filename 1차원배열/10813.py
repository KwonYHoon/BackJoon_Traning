N, M = map(int, input().split())
Array = []
for i in range(1, N + 1):
    Array.append(i)

Switch = 0

for _ in range(M) :
    i, j = map(int, input().split())
    Switch = Array[i - 1]
    Array[i - 1] = Array[j - 1]
    Array[j - 1] = Switch

for a in range(len(Array)):
    print(Array[a], end = " ")
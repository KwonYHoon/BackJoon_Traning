N, M = map(int, input().split())
Array = [0] * (N + 1)

for _ in range(M):
    A, B, C = map(int, input().split())
    for i in range(A, B + 1):
        Array[i] = C

for i in range(1, N + 1):
    print(Array[i], end = " ")
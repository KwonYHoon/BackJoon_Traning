# 색종이

N = int(input())
A = [[0 for _ in range(100)] for _ in range(100)]
area = 0

for i in range(N):
    x, y = list(map(int, input().split()))

    for x_idx in range(x, x + 10):
        for y_idx in range(y, y + 10):
            A[x_idx][y_idx] = 1

for array_row in A :
    area += array_row.count(1)

print(area)
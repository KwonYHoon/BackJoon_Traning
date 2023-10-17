# 최댓값
MAX = 0
locationX, locationY = 0, 0

A = [list(map(int, input().split())) for _ in range(9)]


for i in range(9):
    for j in range(9):
        if(A[i][j] >= MAX):
            MAX = A[i][j]
            locationX = i + 1
            locationY = j + 1

print(MAX)
print(locationX, locationY)
# 세로 읽기
length = []
A = []

for i in range(5):
    A.append(list(input()))
    length.append(len(A[i]))

for i in range(max(length)):
    for j in range(5):
        if(i < length[j]):
            print(A[j][i], end = "")

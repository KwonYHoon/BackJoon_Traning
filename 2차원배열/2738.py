# 행렬 덧셈
# 어려웠던 점 : map으로 나누고 list형으로 append를 해야 
# 연산이 가능한지 몰라서 list형이 아닌 맵핑으로 그냥 값을 
# 넣어 연산이 불가능 했었다.


N, M = map(int, input().split())
A = []
B = []

for _ in range(N) :
    A.append(list(map(int, input().split())))

for _ in range(N) :
    B.append(list(map(int, input().split())))

for i in range(0, N):
    for j in range(0, M):
        print(A[i][j] + B[i][j], end = " ")
    print()
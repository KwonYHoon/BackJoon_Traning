# 킹, 퀸, 룩, 비숍, 나이트, 폰
# 1, 1, 2, 2, 2, 8
A = [1, 1, 2, 2, 2, 8]
N = list(map(int, input().split()))

for i in range(len(N)):
    print(A[i] - N[i], end = " ")
# 진법 변환

N, B = input().split()
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = 0

N = N[::-1]

for i, n in enumerate(N):
    result += (int(B) ** i) * (ary.index(n))

print(result)

# 숏 코딩

n, x = input().split()
print(int(n, int(x)))
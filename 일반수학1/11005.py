# 진법 변환 2

N, B = map(int, input().split())
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ''

while N != 0 :
    result += str(ary[N % B])
    N //= B

print(result[::-1])
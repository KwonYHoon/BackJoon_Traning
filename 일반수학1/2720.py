# 세탁소 사장 동혁

T = int(input())

for _ in range(T):
    money = int(input())
    for i in [25, 10, 5, 1]:
        print(money // i, end = " ")
        money %= i

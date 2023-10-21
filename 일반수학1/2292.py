# 벌집
# 1개, 6개, 12개, 18개, 24개

N = int(input())
num, count = 1, 1

while N > num :
    num += 6 * count
    count += 1

print(count)
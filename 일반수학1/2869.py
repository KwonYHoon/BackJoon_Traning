# 달팽이는 올라가고 싶다

A, B, V = map(int, input().split())
day = 0
height = 0

while True:
    day += 1
    height += A
    if(height >= V):
        print(day)
        break
    height -= B

##########################################

import sys, math

A, B, V = map(int, sys.stdin.readline().split())
day = (V - B) / (A - B)
print(math.ceil(day))
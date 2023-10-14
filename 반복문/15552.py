import sys

Count = int(input())

for i in range(Count):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)
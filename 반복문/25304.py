Price = int(input())
Count = int(input())
Sum = 0

for i in range(Count):
    A, B = map(int, input().split())
    Sum = Sum + A * B

if(Sum == Price): print("Yes")
else: print("No")
A, B, C = map(int, input().split())
cost = 0

if(A == B and B == C):
    cost = 10000 + max(A, B, C) * 1000
elif(A == B and B != C):
    cost = 1000 + B * 100
elif(A != B and B == C):
    cost = 1000 + B * 100
elif(A == C and A != B):
    cost = 1000 + A * 100
elif(A != B and B != C and A != C):
    cost = max(A, B, C) * 100

print(cost)
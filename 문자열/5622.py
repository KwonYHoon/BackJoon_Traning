dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
S = input().upper()
time = 0

for i in range(len(S)):
    for j in dial :
        if(S[i] in j):
            time += dial.index(j) + 3

print(time)
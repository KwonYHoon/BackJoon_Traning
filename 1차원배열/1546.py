N = int(input())
Score = list(map(int, input().split()))
M = max(Score)
for i in range(len(Score)) :
    Score[i] = Score[i] / M * 100

print(sum(Score) / N)
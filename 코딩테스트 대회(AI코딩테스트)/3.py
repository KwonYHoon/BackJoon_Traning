## 지뢰제거병
# DFS 이용
### 지뢰 묶음, 묶음별 몇 개의 지뢰가 있는지 출력

# N 입력, N개의 줄 입력

N = int(input())
graph_Mine = []
count = []
num = []
### 지뢰 그래프 작성 ###
for i in range(N):
    graph_Mine.append(list(map(int, input())))
### dfs 알고리즘을 통해 문제 해결 ###
def dfs(x, y):
    ## x와 y가 범위 밖으로 넘어갔을 경우 False 리턴
    if(x <= -1 or x >= N or y <= -1 or y >= N):
        return False
        
    ## 지뢰가 있는 곳 (1)일 경우
    if(graph_Mine[x][y] == 1):
        num.append(graph_Mine[x][y]) # num 리스트에 지뢰 추가
        graph_Mine[x][y] = 0 # num 리스트에 추가했으면 0으로 제거
        dfs(x - 1, y) # 지뢰의 왼쪽
        dfs(x, y - 1) # 지뢰의 위
        dfs(x + 1, y) # 지뢰의 오른쪽
        dfs(x, y + 1) # 지뢰의 아래
        return True  # 지뢰가 있을 시 True 리턴
    return False

result = 0

for i in range(N):
    for j in range(N):
        if(dfs(i, j)) == True: # 지뢰 탐색을 했을 시
            result += 1 # 지뢰 묶음을 표시하기 위해 result에 카운트
            count.append(len(num)) # num 리스트의 지뢰 갯수를 count리스트에 추가
            num = [] # num 리스트 초기화


print(result) ## 지뢰 묶음 수 출력
count.sort() # 오름차순으로 출력을 위해 정렬

## 각 묶음의 지뢰 갯수를 오름차순으로 출력
for z in range(result):
    print(count[z])
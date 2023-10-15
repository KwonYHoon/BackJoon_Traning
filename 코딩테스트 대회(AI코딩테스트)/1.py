## 덧셈 피라미드

# [[1],   - 1번 Floor 1 : 1
# [1, 1],   - 3번 Floor 2 : 2
# [1, 2, 1],   - 6번 Floor 3 : 4
# [1, 3, 3, 1],  - 10번 Floor 4 : 8
# [1, 4, 6, 4, 1]  - 15번 Floor 5 : 16
# [1, 5, 10, 10, 5, 1]...]  - 21번 Floor 6 : 32

floor = []
lines = []

select_floor = int(input()) # 원하는 층 입력

# 1층, 2층은 for문을 통해 1을 N층에 맞게 lines에 삽입
# 후에 floor에 해당 층에 맞게 삽입 [[1], [1, 1]]
for line_idx in range(1, select_floor + 1) :
    if(line_idx <= 2):
        lines = []
        for i in range(line_idx):
            lines.append(1)
        floor.append(lines)
    else:
        lines = []
        # 층 마다 맨 앞, 맨 뒤에 1을 추가해줘야 하므로 for문 앞뒤로 1을 삽입
        lines.append(1)
        # 전 층의 list를 가져와 인덱스 [0] + [1], [1] + [2], ...
        # 계산 된 값이 lines 리스트에 들어있게 된다.
        for i in range(line_idx - 2):
            lines.append(floor[line_idx - 2][i] + floor[line_idx - 2][i + 1])
        lines.append(1)
        floor.append(lines) # lines에 있는 리스트 floor에 삽입

# print(floor) ## 각 층별로 생성된 피라미드 출력

print(sum(floor[-1])) # floor 리스트 마지막 인덱스의 합을 출력

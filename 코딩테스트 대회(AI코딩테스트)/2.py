## 2번 멱함수의 합
# x^1 + x^2 + x^3 + x^4 + ...

# 입력 1. n의 갯수
# 입력 2. n개의 양수, 음수

# 목적 : 최대값 출력 / 그리디 알고리즘 활용

sum = 0

n = int(input()) # 입력 받을 숫자 갯수 입력
num_list = list(map(int, input().split(' '))) # n개의 숫자 입력 후 정렬
num_list.sort()

for i in range(n, 0, -1):
    if(i%2 == 0): ### 짝수 ###
        if(abs(min(num_list)) >= max(num_list)): ## 절댓값이 가장 작은 값이 가장 큰 값 보다 클 때
            sum += num_list[0] ** i # 가장 작은 값을 n제곱 후 pop을 통해 제거
            num_list.pop(0)
        else: ## 절댓값이 가장 큰 값이 가장 작은 값 보다 클 때
            sum += num_list[-1] ** i # 가장 큰 값을 n제곱 후 pop을 통해 제거
            num_list.pop()
    else: ### 홀수 ###
        sum += num_list[-1] ** i # 가장 큰 값을 n제곱 후 pop을 통해 제거
        num_list.pop()

print(sum)

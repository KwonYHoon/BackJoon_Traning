# 단어 공부

S = input().upper()
S_list = list(set(S))
cnt = []

for i in S_list :
    cnt.append(S.count(i))

if(cnt.count(max(cnt)) > 1):
    print("?")
else:
    print(S_list[(cnt.index(max(cnt)))])
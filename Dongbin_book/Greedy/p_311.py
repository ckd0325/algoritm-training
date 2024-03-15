# 팁: 오름차순으로 모험가 정렬하고 앞부터 처리

n = int(input())
adv = list(map(int, input().split()))
adv.sort()

count = 0 # 그룹에 포함되는 모험자 수
result = 0 # 전체 그룹 수

for i in adv: # 공포도가 낮은 모험가부터 확인
  count += 1 # 해당 모험가 그룹에 포함 시킴
  if count >= i: # 만약 그룹 내 모험가 수가 현재 모험가의 공포도 이상이라면
    result += 1 # 그룹 하나 만들기
    count = 0 # 그룹 내 모험가 수 초기화

print(result)
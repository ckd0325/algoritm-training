score = input()

left = [] # 왼쪽 자릿수가 담길 리스트
right = [] # 오른쪽 자릿수가 담길 리스트

for i in range(len(score)//2): # 왼쪽 자릿수의 담기
  left.append(int(score[i]))

for i in range(len(score)//2, len(score)): # 오른쪽 자릿수 담기
  right.append(int(score[i]))

if sum(left) == sum(right): # 왼쪽, 오른쪽 자릿수 합이 동일하면 LUCKY 출력
  print("LUCKY")
else:
  print("READY")
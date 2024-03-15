# 어떤 경우에 + 연산이 필요할지 생각해보기

string = input()
nums = [] # 입력에 대한 수가 담길 리스트
result = 0 # 연산결과

for c in string: # 입력 문자열을 하나씩 떼어 리스트에 삽입
 nums.append(int(c))

for n in nums: # 리스트에 수를 하나씩 빼면서
  if result <= 1 or n <= 1: # 이전 결과값이나 현재 수 중 하나라도 1이하 이면 더하기 연산
    result += n
  else: # 이외의 경우에는 곱하기 연산
    result *= n

print(result)
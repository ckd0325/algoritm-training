string = input() # 입력받기
chars = [] # 입력 문자열을 문자로 나누어 담을 배열
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] # 숫자의 문자 타입 리스트
result = "" # 결과가 담길 문자열
sum_val = 0 # 숫자 문자의 합이 담길 변수

for c in string: # 문자열을 순회하며 문자 리스트에 담기
  chars.append(c)

chars.sort() # 문자 리스트 정렬

for c in chars: # 문자 리스트 순회
  if c in numbers: # 만약 현재 문자가 숫자라면
    sum_val += int(c) # 숫자 문자 합 변수에 더하기
  else: # 숫자 문자가 아니라면 결과 문자열에 더하기
    result += c

print(result + str(sum_val)) # result와 sum_val을 합치기
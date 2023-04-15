# 00:00:00 부터 n:00:00까지의 시간 중 3이 하나라도 포함되어 있는 모든 경우의 수

n = int(input())
ans = 0
count = 0

for minute in range(1, 61):
    for sec in range(1, 61):
        if '3' in str(minute)+str(sec):
            count += 1

for i in range(0, n+1):
    if i in [3, 13, 23]:
        ans += 3600
    else:
        ans += count

print(ans)

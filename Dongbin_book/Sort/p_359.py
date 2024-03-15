n = int(input())
scores = []

for _ in range(n):
    n, k, e, m = input().split()
    k, e, m = map(int, [k,e, m])
    scores.append((n, k, e, m))

scores.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for s in scores:
    print(s[0])
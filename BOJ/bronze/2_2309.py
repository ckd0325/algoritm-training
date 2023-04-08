# https://www.acmicpc.net/problem/2309

def sol(dwarfs: list):
    for i in range(8):
        for j in range(i+1,9):
            if i == j: continue
            if sum(dwarfs) - dwarfs[i] - dwarfs[j] == 100:
                fake1 = dwarfs[i]
                fake2 = dwarfs[j]
                dwarfs.remove(fake1)
                dwarfs.remove(fake2)
                return dwarfs
            
dwarfs = [int(input()) for _ in range(9)]

for i in sorted(sol(dwarfs)):
    print(i)
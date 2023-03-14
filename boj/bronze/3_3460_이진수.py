test_count = int(input())

bins = [int(input()) for _ in range(test_count)]

for i in bins:
    count = 0
    idx = []

    while True:
        if i % 2 == 1:
            idx.append(count)
        
        i //= 2
        
        if(i == 0): break
        count += 1

    print(*idx)
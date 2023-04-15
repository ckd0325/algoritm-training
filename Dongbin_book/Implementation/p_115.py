coord = input()
x, y = coord[0], int(coord[1])

count = 0
row = range(1, 9).index(y)
col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].index(x)

steps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

for step in steps:
    x_res = col + step[0]
    y_res = row + step[1]
    if x_res < 0 or x_res > 7 or y_res < 0 or y_res > 7:
        continue
    count += 1

print(count)





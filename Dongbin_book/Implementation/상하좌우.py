n = int(input())
plan = input().split()

x = 1
y = 1
x_history = 1
y_history = 1

for i in plan:
    if i == 'L':
        x -= 1
    elif i == 'R':
        x += 1
    elif i == 'U':
        y -= 1
    else:
        y += 1

    if x > n or x < 1 or y > n or y < 1:
        x = x_history
        y = y_history
    x_history = x
    y_history = y

print(y, x)


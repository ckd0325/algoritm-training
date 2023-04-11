# p.87

def ans1():
    change = int(input())

    coin = [500, 100, 50, 10]
    i = 0
    count = 0

    while i < len(coin):
        if change - coin[i] >= 0:
            count += 1
            change -= coin[i]
        else:
            i += 1

    print(count)


def ans2():
    change = int(input())
    count = 0

    coin_type = [500, 100, 50, 10]

    for coin in coin_type:
        count += change // coin
        change %= coin

    print(count)

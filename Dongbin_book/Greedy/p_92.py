# p.92

def ans1():
    n, m, k = map(int, input().split())
    arr = list(map(int,input().split()))
    ans = 0
    k_count = 0

    arr.sort(reverse=True)

    for i in range(1, m+1):
        if k_count == k:
            num = 0
            ans += arr[1]
        else:
            k_count += 1
            ans += arr[0]

    print(ans)


def ans2():
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    first = arr[0]
    second = arr[1]

    iter_count = m // (k+1)
    mod_val = m % (k+1)

    ans = (first*k + second) * iter_count + first*mod_val
    print(ans)


# 자연수로 이뤄진 크기 n의 배열이 주어졌을 때,
# 각 요소 값들을 이용해 m번의 덧셈을 했을 때 나올 수 있는 최댓값 구하기
# 이 때, 동일한 인덱스의 값은 k번 보다 많이 연속될 수 없다.

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

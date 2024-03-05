# p.182
# 팁: 정렬 메소드를 잘 이용하자
# 의문점: 책의 답이라면 무조건 같은 인덱스의 값끼리만 비교하게 되지 않을까?

def my_answer():
    n, k = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    arr1.sort()
    arr2.sort(reverse=True)

    count = 0
    for i in range(n):
        if count >= k:
            break
        if arr1[i] < arr2[count]:
            arr1[i], arr2[count] = arr2[count], arr1[i]
            count += 1


    print(sum(arr1))

def book_answer():
    n, k = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    arr1.sort()
    arr2.sort(reverse=True)

    for i in range(k):
        if arr1[i] < arr2[i]:
            arr1[i], arr2[i] = arr2[i], arr1[i]
        else:
            break

my_answer()
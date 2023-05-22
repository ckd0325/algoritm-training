# https://school.programmers.co.kr/learn/courses/30/lessons/42577

"""
풀이 포인트

    solution1: phone_book을 정렬하면 번호 크기 순으로 정렬이 된다.
    그러므로 현재 인덱스의 값과 다음 인덱스의 값에서 현재 인덱스의 길이만큼 슬라이싱하여 비교하면 됨

    solution2: 해시를 이용한 정석적인 풀이. phone_book의 요소를 키로 하는 딕셔너리 생성.
    이후 phone_book의 번호를 하나씩 꺼내면서 한 글자씩 temp에 붙인다.
    그러다가 temp가 현재 꺼낸 번호가 아니고 temp 값이 딕셔너리의 키 값에 존재한다면 이는 temp라는 더 짧은 번호가 존재한다는 뜻
"""
def solution1(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            answer = False
    return answer


def solution2(phone_book):
    hash_map = {num: 1 for num in phone_book}

    for num in phone_book:
        temp = ""
        for c in num:
            temp += c
            if temp in hash_map and temp != num:
                return False

    return True
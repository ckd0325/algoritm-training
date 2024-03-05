# p.180
# 팁: 기본 정렬 메소드의 'key' 속성을 이용하자

def setting(data):
  return data[1]

def sort(arr):
  return sorted(arr, key=setting, reverse=True)

def my_answer():
    n = int(input())
    array = []

    for _ in range(n):
        n, s = input().split()
        name = n
        score = int(s)
        array.append((name, score))

    for i in sort(array):
        print(i[0], end=" ")


def book_answer():
    n = int(input())

    array = []
    for i in range(n):
        input_data = input.split()
        array.append(input_data[0], int(input_data[1]))

    array = sorted(array, key=lambda student: student[1])

    for student in array:
        print(student[0], end=" ")
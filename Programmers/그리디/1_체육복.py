# https://school.programmers.co.kr/learn/courses/30/lessons/42862

"""
풀이 포인트:

lost와 reserve는 정렬하는게 맘 편하다.
우선 여분을 가져온 학생이 도둑을 맞은 경우, 이 학생은 여분을 안 챙긴 학생과 똑같이 처리
그러므로 lost와 reserve에서 없애준다고 생각
본인은 여분이 있는 학생의 체육복 개수 현황을 dict를 이용해 저장하였음
어쨌든 이후 lost에 있는 학생 양 옆을 살피면서 여분을 얻을 수 있는지 여부를 파악
"""
def solution(n, lost, reserve):
    lost = sorted(lost)
    not_num = 0
    r_dict = {}

    for r in reserve:
        r_dict[r] = 2

    r_dict_keys = list(r_dict.keys())
    r_dict = dict(filter(lambda item: item[0] not in lost, r_dict.items()))
    lost = list(filter(lambda x: x not in r_dict_keys, lost))

    r_dict_keys = list(r_dict.keys())

    for l in lost:
        if l - 1 in r_dict_keys and r_dict[l - 1] == 2:
            r_dict[l - 1] -= 1
        elif l + 1 in r_dict_keys and r_dict[l + 1] == 2:
            r_dict[l + 1] -= 1
        else:
            not_num += 1

    return n - not_num

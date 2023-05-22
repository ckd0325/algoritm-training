# https://school.programmers.co.kr/learn/courses/30/lessons/12909

"""
풀이 포인트:

'(', ')'의 수는 동일해야 한다. 그러므로 s의 문자를 하나씩 stack에 넣어줄 때,
')'가 append 되면 pop()을 2번 해준다. 올바른 괄호라면 순회가 끝났을 때 비어있을 것이다.
')'가 더 많을 경우에는 IndexError가 발생할 수 있으니 예외처리가 필요하다.
"""

from collections import deque


def solution(s):
    answer = True
    queue = deque()

    if s[0] == ')' or s[-1] == '(':
        return False

    for b in s:
        queue.append(b)
        if b == ')':
            try:
                queue.pop()
                queue.pop()
            except Exception:
                return False

    if queue:
        return False
    return True

from collections import deque


def solution(dartResult):
    answer = 0
    items = deque(dartResult)
    before_point = 0

    while items:
        item = items.popleft()
        if item != 'S' and item != 'D' and item != 'T' and item != '*' and item != '#':
            next_item = items.popleft()
            if next_item != 'S' and next_item != 'D' and next_item != 'T' and next_item != '*' and next_item != '#':
                point = int(item + next_item)
            else:
                point = int(item)
                items.appendleft(next_item)
        else:
            if item == 'S' or item == 'D' or item == 'T':
                if item == 'S':
                    point = point
                elif item == 'D':
                    point = point ** 2
                else:
                    point = point ** 3

                if items:
                    mode = items.popleft()
                    if mode == '*':
                        point = point * 2
                        answer -= before_point
                        before_point = before_point * 2
                        answer = answer + before_point + point
                    elif mode == '#':
                        point = -point
                        answer = answer + point

                    else:
                        items.appendleft(mode)
                        answer = answer + point
                else:
                    answer = answer + point

                before_point = point

    return answer

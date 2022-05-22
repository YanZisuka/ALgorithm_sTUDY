from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        case = []

        for order in orders:
            order = sorted(list(order))
            case += list(combinations(order, i))

        case = list(set(case))
        cnt = [0] * len(case)

        for c in range(len(case)):
            for o in orders:
                if set(case[c]) == set(case[c]) & set(o):
                    cnt[c] += 1

        if cnt and max(cnt) >= 2:
            for i in range(len(cnt)):
                if cnt[i] == max(cnt):
                    answer.append(''.join(case[i]))

    answer.sort()
    return answer
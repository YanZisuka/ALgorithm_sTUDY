from itertools import combinations


def solution(relation):
    result = 0
    com_list = []
    row = len(relation[0])

    # 1개로 후보키가 될 수 있는 경우
    column = [['T'] for _ in range(row)]
    for r in relation:
        for i in range(row):
            if r[i] in column[i]:
                column[i][0] = 'F'
            column[i].append(r[i])

    for r in range(row):
        if column[r][0] == 'T':
            result += 1
        else:
            com_list.append(r)

    for i in range(2, len(com_list) + 1):
        case = list(combinations(com_list, i))
        print(case)

    answer = 0
    return answer
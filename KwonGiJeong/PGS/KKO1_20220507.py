def solution(survey, choices):
    table = []
    for i in range(len(survey)):
        q = list(survey[i])
        point = choices[i] - 4
        if point < 0:
            for j in range(-point):
                table.append(q[0])
        else:
            for j in range(point):
                table.append(q[1])

    answer = ''
    
    if table.count('R') >= table.count('T'):
        answer = answer + 'R'
    else:
        answer = answer + 'T'

    if table.count('C') >= table.count('F'):
        answer = answer + 'C'
    else:
        answer = answer + 'F'

    if table.count('J') >= table.count('M'):
        answer = answer + 'J'
    else:
        answer = answer + 'M'

    if table.count('A') >= table.count('N'):
        answer = answer + 'A'
    else:
        answer = answer + 'N'

    return answer
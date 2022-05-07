def solution(survey, choices):
    answer = ''
    stat = {i: 0 for i in range(1, 5)}
    pluses = ['T', 'F', 'M', 'N']
    minuses = ['R', 'C', 'J', 'A']
    score = {
        1: -3,
        2: -2,
        3: -1,
        4: 0,
        5: 1,
        6: 2,
        7: 3,
    }
    reverse_score = {
        1: 3,
        2: 2,
        3: 1,
        4: 0,
        5: -1,
        6: -2,
        7: -3,
    }

    for i in range(len(survey)):
        n, m = list(survey[i])
        if n in pluses:
            stat_idx = pluses.index(n) + 1

            choice = choices[i]
            stat[stat_idx] += reverse_score[choice]

        else:
            stat_idx = minuses.index(n) + 1

            choice = choices[i]
            stat[stat_idx] += score[choice]

    for k, v in stat.items():
        if v > 0:
            answer += pluses[k-1]
        elif v < 0:
            answer += minuses[k-1]
        else:
            a, b = pluses[k-1], minuses[k-1]
            if ord(a) < ord(b):
                answer += a
            else:
                answer += b

    return answer




print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))  # "TCMA"
print(solution(["TR", "RT", "TR"], [7, 1, 3]))  #  "RCJA"

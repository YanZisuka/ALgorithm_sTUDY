def get_point(p, num):
    point = 0
    for cnt in range(1, num + 1):
        if p % cnt:
            point += (p // cnt) + 1
        else:
            point += (p // cnt)
    return point

def solution(p, vs):

    IDs = []
    table = []
    vs_list = []
    set_vs = []

    for pair in vs:
        pair_lists = pair.split(':')
        vs_list.append(pair_lists)
        if not pair_lists in table:
            table.append(pair_lists)
        for ID in pair_lists:
            IDs.append(ID)

    IDs = sorted(list(set(IDs)))

    win_cnts = []
    for i in range(len(table)):
        win_cnts.append(vs_list.count(table[i]))

    point_table = []
    for win_cnt in win_cnts:
        point_table.append(get_point(p, win_cnt))

    point_scores = [0] * len(IDs)
    for i in range(len(IDs)):
        for j in range(len(table)):
            if table[j][0] == IDs[i]:
                point_scores[i] += point_table[j]

    win_scores = [0] * len(IDs)
    for i in range(len(IDs)):
        for j in range(len(table)):
            if table[j][0] == IDs[i]:
                win_scores[i] += 1

    winner_idx = 0
    winner_point = point_scores[0]
    winner_win = win_scores[0]
    if len(IDs) > 1:
        for i in range(1, len(IDs)):
            if winner_point < point_scores[i]:
                winner_idx = i
                winner_point = point_scores[i]
                winner_win = win_scores[i]
            elif winner_point == point_scores[i]:
                if winner_win < win_scores[i]:
                    winner_idx = i
                    winner_point = point_scores[i]
                    winner_win = win_scores[i]

    answer = IDs[winner_idx]
    return answer
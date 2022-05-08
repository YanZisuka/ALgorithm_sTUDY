def solution(id_list, report, k):
    answer = []
    to_dic = {}
    from_dic = {}

    for i in id_list:
        to_dic[i] = 0
        from_dic[i] = [0]

    for r in set(report):
        from_id, to_id = r.split()
        to_dic[to_id] += 1
        from_dic[from_id].append(to_id)

    for f in from_dic.keys():
        for v in from_dic[f][1:]:
            if to_dic[v] >= k:
                from_dic[f][0] += 1

        answer.append(from_dic[f][0])

    return answer
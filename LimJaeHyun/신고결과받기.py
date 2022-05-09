def solution(id_list, report, k):
    report = list(set(report))
    reported_dict = dict(zip(id_list, [[] for _ in range(len(id_list))]))
    reporter_dict = dict(zip(id_list, [0 for _ in range(len(id_list))]))

    for case in report:
        reporter, reported = case.split(' ')
        reported_dict[reported].append(reporter)

    for user in reported_dict:
        if len(reported_dict[user]) >= k:
            for name in reported_dict[user]:
                reporter_dict[name] += 1

    answer = list(reporter_dict.values())

    return answer
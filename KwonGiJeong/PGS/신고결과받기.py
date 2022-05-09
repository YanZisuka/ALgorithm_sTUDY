def solution(id_list, report, k):
    real_report = list(set(report))
    reported_cnt = {x:0 for x in id_list}
    answer = [0] * len(id_list)
    
    for one_report in real_report:
        reported_cnt[one_report.split()[1]] += 1
            
    for one_report in real_report:
        if reported_cnt[one_report.split()[1]] >= k:
            answer[id_list.index(one_report.split()[0])] += 1
    
    return answer
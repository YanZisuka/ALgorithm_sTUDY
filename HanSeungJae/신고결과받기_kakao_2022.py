def solution(id_list, report, k):
    n = len(id_list)
    answer = []
    id_mat = [[0, [], 0, 0] for _ in range(n)]
    report = set(report)
    id_dict = {}
    
    for i in range(n):
        id_mat[i][0] = id_list[i]
        id_dict.setdefault(id_list[i], i)
        
    while report:
        ff, tt = report.pop().split(' ')
        id_mat[id_dict.get(ff)][1].append(tt)
        id_mat[id_dict.get(tt)][2] += 1  # 신고받은 횟수
        
    # for i in range(m):
    #     ff, tt = report[i].split(' ')
    #     for j in range(n):
    #         if id_mat[j][0] == ff:
    #             id_mat[j][1].append(tt)
    #         elif id_mat[j][0] == tt:
    #             id_mat[j][2] += 1  # 신고받은 횟수
                
    for i in range(n):
        if id_mat[i][2] >= k:
            for j in range(n):
                if id_mat[i][0] in id_mat[j][1]:
                    id_mat[j][3] += 1  # 메일받는 횟수
                    
    for i in range(n):
        answer.append(id_mat[i][3])
        
    return answer
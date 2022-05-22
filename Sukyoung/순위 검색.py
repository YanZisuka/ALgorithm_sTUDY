def solution(info, query):
    answer = []
    applicant = []
    ask_list = []
    for i in info:
        applicant.append(i.split())
    for q in query:
        ask = q.split(' and ')
        ask[-1] = ask[-1].split()
        ask = ask[:-1] + ask[-1]
        ask_list.append(ask)

    applicant.sort(key=lambda x: int(x[4]), reverse=True)

    def ok(a):
        cnt = 0
        for ap in applicant:
            if int(ap[4]) >= int(a[4]):
                if a[0] == '-' or a[0] == ap[0]:
                    if a[1] == '-' or a[1] == ap[1]:
                        if a[2] == '-' or a[2] == ap[2]:
                            if a[3] == '-' or a[3] == ap[3]:
                                cnt += 1
            else:
                return cnt
        return cnt

    for a in ask_list:
        answer.append(ok(a))

    return answer
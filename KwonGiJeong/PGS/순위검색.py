def solution(info, query):
    answer = []
    for query_str in query:
        query_list = list(query_str.split(' and '))
        query_list.extend(list((query_list.pop()).split(' ')))

        cnt = 0

        for info_str in info:
            info_list = list(info_str.split(' '))

            if query_list[0] == '-' or query_list[0] == info_list[0]:
                if query_list[1] == '-' or query_list[1] == info_list[1]:
                    if query_list[2] == '-' or query_list[2] == info_list[2]:
                        if query_list[3] == '-' or query_list[3] == info_list[3]:
                            if int(info_list[4]) >= int(query_list[4]):
                                cnt += 1
        answer.append(cnt)

    return answer

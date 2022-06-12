# def solution(N, stages): 망작
#     answer = []
#     failure_rate = []
#     for i in range(1, N + 1):
#         total_players = len(stages)
#         cnt = 0
#         for player in stages:
#             if player <= i:
#                 cnt += 1
#         failure_rate.append([i, cnt/total_players])
#         while i in stages:
#             stages.remove(i)
#     failure_rate.sort(key=lambda x: x[1], reverse=True)
#     for order in failure_rate:
#         answer.append(order[0])
#     print(answer)
#     return answer


def solution(N, stages):
    answer = []
    failure_rate = []
    for i in range(1, N + 1):
        total_players = 0
        cnt = 0
        for player in stages:
            if player >= i:
                total_players += 1
            if i-1 < player <= i:
                cnt += 1
        failure_rate.append([i, cnt/total_players]) if total_players != 0 else failure_rate.append([i, 0])
    failure_rate.sort(key=lambda x: x[1], reverse=True)
    for order in failure_rate:
        answer.append(order[0])
    print(failure_rate)
    print(answer)
    return answer


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
solution(4, [4, 4, 4, 4, 4])

def solution(lottos, win_nums):
    answer = []
    table = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    
    cnt = 0
    zcnt = lottos.count(0)
    for num in win_nums:
        if num in lottos:
            cnt += 1
    answer.append(table[cnt + zcnt])
    answer.append(table[cnt])
    return answer
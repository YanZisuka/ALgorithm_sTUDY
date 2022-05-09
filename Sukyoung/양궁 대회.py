def solution(n, info):
    # 어피치가 획득한 점수
    apeach = []
    for i in range(11):
        if info[i] > 0:
            apeach.append(10-i)

    # 라이언이 이기기 위해 필요한 점수
    lion_win = [i+1 for i in info]
    win_case = []
    for r in range(11):
        win_case.append([lion_win[r],10-r])  # [횟수,점수]

    dp = [[[0]]*(n+1) for _ in range(11)]

    for i in range(1,11):
        bow = win_case[i-1][0]
        score =  win_case[i-1][1]
        for j in range(1,n+1):
            if j < bow:
                dp[i][j] = dp[i-1][j]

            else:
                case1 = (set(apeach) - set(dp[i-1][j]))  # 어피치가 얻을 수 있는 점수
                case2 = (set(apeach) - set(dp[i-1][j-bow]+ [score]))
                if (sum(dp[i-1][j])-sum(case1))>(sum(dp[i-1][j-bow]+ [score]) - sum(case2)):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-bow]+ [score]

    final_apeach = sum(set(apeach) - set(dp[i][j]))  # 최종 어피치 점수
    final_lion = sum(dp[i][j])  # 최종 라이언 점수

    if final_apeach >= final_lion:  # 라이언이 어피치를 이길 수 없는 경우
        answer = [-1]
    else:
        answer = [0]*11
        win_case.reverse()
        result = dp[i][j][1:]
        for point in result:
            answer[point] = win_case[point][0]

        answer.reverse()
        if sum(answer) != n:  # 화살이 남았을 경우 0점에 맞춘걸로
            answer[-1] = n-sum(answer)

    return answer
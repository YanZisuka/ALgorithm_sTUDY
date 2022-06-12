def solution(N, stages):
    answer = []
    stages.sort()

    for n in range(1, N + 1):
        cnt = 0
        for s in range(len(stages)):
            if stages[s] > n:
                break
            else:
                cnt += 1
        if len(stages) == 0:
            answer.append([n, 0])
        else:
            answer.append([n, cnt / len(stages)])

        if s == len(stages) - 1:
            stages = []
        else:
            stages = stages[s:]

    answer.sort(reverse=True, key=lambda x: (x[1]))
    answer = [i[0] for i in answer]

    return answer
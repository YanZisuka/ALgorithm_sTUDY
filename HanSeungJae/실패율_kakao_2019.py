def solution(N, stages):
    answer = []
    tmp = []
    challengers = [0] * (N+2)
    failures = [0] * (N+2)
    
    for i in range(len(stages)):
        for j in range(1, stages[i]+1):
            challengers[j] += 1
        failures[stages[i]] += 1
        
    for i in range(1, N+1):
        if challengers[i] == 0:
            failRate = 0
        else:
            failRate = failures[i]/challengers[i]
        tmp.append((i, failRate))
    
    tmp.sort(key=lambda x: (-x[1], x[0]))
    
    for i in range(len(tmp)):
        answer.append(tmp[i][0])
    
    return answer
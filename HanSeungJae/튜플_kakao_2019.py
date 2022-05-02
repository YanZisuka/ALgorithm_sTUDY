def solution(s):
    answer = []
    s = s[1:-1]
    sets = []
    n = len(s)
    i = 0
    
    while i < n:
        if s[i] == '{':
            for j in range(i+1, n):
                if s[j] == '}':
                    sets.append(s[i:j+1])
                    i = j
                    break
        i += 1
                    
    sets = list(map(lambda x: x[1:-1], sets))
    sets = list(map(lambda x: x.split(','), sets))
    sets.sort(key=lambda x: len(x))
    
    for se in sets:
        for num in se:
            num = int(num)
            if num not in answer:
                answer.append(num)
    
    return answer
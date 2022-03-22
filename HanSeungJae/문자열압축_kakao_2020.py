def solution(s):
    answer = float('inf')
    d = 1
    
    if len(s) == 1:
        return 1
    
    while d <= len(s) // 2:
        new_s = []
        cnt = 1
        for i in range(0, len(s), d):
            if s[i:i+d] == s[i+d:i+2*d]:
                cnt += 1
            else:
                if cnt == 1:
                    new_s.append(f'{s[i:i+d]}')
                else:
                    new_s.append(f'{cnt}{s[i:i+d]}')
                    cnt = 1
                    
        new_s = ''.join(new_s)
        answer = min(answer, len(new_s))
        d += 1
        
    return answer
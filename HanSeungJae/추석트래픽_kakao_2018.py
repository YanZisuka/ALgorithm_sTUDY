def solution(lines):
    answer = 0
    starts = []
    ends = []
    
    for i in range(len(lines)):
        s, t = int(lines[i][11:13])*3600*1000 + int(lines[i][14:16])*60*1000 + float(lines[i][17:23])*1000, float(lines[i][24:-1])*1000
    
        starts.append(s - t + 1)
        ends.append(s)
        
    for start in starts:
        cnt = 0
        for i in range(len(starts)):
            if ends[i] < start or starts[i] > start+999:
                pass
            else:
                cnt += 1
        answer = max(answer, cnt)
        
    for end in ends:
        cnt = 0
        for i in range(len(ends)):
            if ends[i] < end or starts[i] > end+999:
                pass
            else:
                cnt += 1
        answer = max(answer, cnt)

    return answer
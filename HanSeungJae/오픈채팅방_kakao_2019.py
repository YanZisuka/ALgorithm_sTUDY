def solution(record):
    answer = []
    dictTable = {}
    
    for i in range(len(record)):
        st = record[i].split()
        status = st[0]
        userid = st[1]
    
        if status == 'Enter':
            username = st[2]
            dictTable[userid] = username
            answer.append([userid, '님이 들어왔습니다.'])
        elif status == 'Leave':
            answer.append([userid, '님이 나갔습니다.'])
        elif status == 'Change':
            username = st[2]
            dictTable[userid] = username

    for i in range(len(answer)):
        userid, message = answer[i]
        userid = dictTable[userid]
                          
        answer[i] = userid + message
            
    return answer
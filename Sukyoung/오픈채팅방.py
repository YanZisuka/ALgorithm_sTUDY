def solution(record):
    answer = []
    user = {}
    log = []
    for r in record:
        if r[0] == 'L':
            act, user_id = r.split()
            log.append(['Leave', user_id])

        else:
            act, user_id, user_name = r.split()
            user[user_id] = user_name
            if act == 'Enter':
                log.append(['Enter', user_id])

    for l in log:
        if l[0] == 'Enter':
            answer.append(f'{user[l[1]]}님이 들어왔습니다.')
        else:
            answer.append(f'{user[l[1]]}님이 나갔습니다.')

    return answer
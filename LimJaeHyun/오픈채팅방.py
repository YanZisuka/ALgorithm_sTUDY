def solution(record):
    answer = []
    user_info = {}
    record_list = []
    for log in record:
        record_list.append(list(log.split()))
    for log in record_list:
        if log[0] == 'Enter':
            user_info[log[1]] = log[2]
        elif log[0] == 'Change':
            user_info[log[1]] = log[2]
    for log in record_list:
        if log[0] == 'Enter':
            answer.append(f'{user_info[log[1]]}님이 들어왔습니다.')
        elif log[0] == 'Leave':
            answer.append(f'{user_info[log[1]]}님이 나갔습니다.')
    return answer


solution(["Enter uid1234 Muzi",
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Enter uid1234 Prodo",
          "Change uid4567 Ryan"])

def solution(user_id, banned_id):
    lst = [[] for _ in range(len(banned_id))]
    cases = []
    
    for i in range(len(banned_id)):
        ban = banned_id[i]
        for j in range(len(user_id)):
            user = user_id[j]
            if len(ban) != len(user):
                continue
            
            else:
                cnt = 0
                for k in range(len(ban)):
                    if ban[k] != '*':
                        if ban[k] != user[k]:
                            break
                        else:
                            cnt += 1
                    else:
                        cnt += 1
                if cnt == len(ban):
                    lst[i].append(user)  # id 비교
    
    def dfs(n, member):
        if n == len(banned_id):
            cases.append(list(member))
            return

        for i in range(len(lst[n])):
            if lst[n][i] not in member:
                member.append(lst[n][i])
                dfs(n+1, member)
                member.pop()
    
    dfs(0, [])
    
    for i in range(len(cases)):
        cases[i].sort()
    
    cases = list(set([tuple(set(case)) for case in cases]))
        
    answer = len(cases)
    return answer
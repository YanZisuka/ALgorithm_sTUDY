from collections import deque

def solution(n, info):

    def bfs(n, info):
        res = []
        q = deque([(0, [0] * 11)])
        max_diff = 0

        while q:
            target, arrow = q.popleft()

            if sum(arrow) == n:
                appeach, lion = 0, 0
                for i in range(11):
                    if not (info[i] == 0 and arrow[i] == 0):
                        if info[i] >= arrow[i]:
                            appeach += 10 - i
                        else:
                            lion += 10 - i
                if appeach < lion:
                    diff = lion - appeach
                    if max_diff > diff: continue
                    else:
                        max_diff = diff
                        res.clear()
                    res.append(arrow)

            elif sum(arrow) > n: continue

            elif target == 10:
                tmp = arrow[:]
                tmp[target] = n - sum(tmp)
                q.append((-1, tmp))

            else:
                tmp = arrow[:]
                tmp[target] = info[target] + 1
                q.append((target + 1, tmp))
                tmp2 = arrow[:]
                tmp2[target] = 0
                q.append((target + 1, tmp2))
        return res

    answer = bfs(n, info)

    if not answer: return [-1]
    elif len(answer) == 1: return answer[0]
    else: return answer[-1]





print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))  # [0,2,2,0,1,0,0,0,0,0,0]
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))  # [-1]
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))  # [1,1,2,0,1,2,2,0,0,0,0]
print(solution(10, 	[0,0,0,0,0,0,0,0,3,4,3]))  # [1,1,1,1,1,1,1,1,0,0,2]
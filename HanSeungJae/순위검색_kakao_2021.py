from itertools import combinations


def solution(info, query):

    def binary_search(arr, x):
        st, en = 0, len(arr)-1
        while st <= en:
            mid = (st + en) // 2
            if arr[mid] >= x: st = mid + 1
            else: en = mid - 1
        return en + 1

    answer = []
    table = {'all': []}

    info = list(map(lambda x: [i for i in x.split()], info))
    info.sort(key=lambda x: -int(x[-1]))

    for i in info:
        score = int(i.pop())
        for j in range(1, 5):
            for c in combinations(i, j):
                key = ''.join(sorted(list(c)))
                if table.get(key): table[key].append(score)
                else: table[key] = [score]
        table['all'].append(score)

    for q in query:
        qstring = [s for s in q.split() if s != 'and' and s != '-']
        qscore = int(qstring.pop())
        key = ''.join(sorted(qstring)) if qstring else 'all'
        answer.append(binary_search(table[key], qscore) if table.get(key) else 0)

    return answer





print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
# [1,1,1,1,2,4]
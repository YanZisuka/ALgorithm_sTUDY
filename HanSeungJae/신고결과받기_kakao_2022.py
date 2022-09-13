def solution(id_list, report, k):
    answer = [0] * len(id_list)
    table = {id: set() for id in id_list}
    for r in report:
        ff, tt = r.split()
        table[tt].add(ff)

    for v in table.values():
        if len(v) >= k:
            for ff in v:
                answer[id_list.index(ff)] += 1

    return answer




print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
from itertools import combinations

def solution(relation):

    def check(table, case):
        for v in table.values():
            if len(v) > 1: return
        answer.append([c for c in case])

    answer = []
    cols = [i for i in range(len(relation[0]))]

    for i in range(1, len(relation[0]) + 1):
        for case in combinations(cols, i):
            table = {}
            for r in relation:
                key = tuple([r[c] for c in case])
                if not table.get(key): 
                    table[key] = [r]
                else:
                    table[key].append(r)
            
            check(table, case)

    for i, a in enumerate(answer):
        a_set = set(a)
        for j, b in enumerate(answer[i+1:]):
            b_set = set(b)
            if a_set < b_set:
                answer[i+j+1] = [-1]

    while [-1] in answer:
        answer.remove([-1])

    return len(answer)





#  2
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

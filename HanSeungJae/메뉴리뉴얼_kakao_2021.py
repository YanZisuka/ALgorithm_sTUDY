from itertools import combinations

def solution(orders, course):
    answer = []
    menus = {}

    for order in orders:
        for i in range(1, len(order) + 1):
            for comb in combinations(order, i):
                c = ''.join(sorted(list(comb)))
                if menus.get(c):
                    menus[c] += 1
                else:
                    menus[c] = 1 

    for num in course:
        candidates = []
        for k, v in menus.items():
            if len(k) == num:
                candidates.append([k, v])
        
        candidates.sort(key=lambda x: -x[1])
        if candidates:
            s = candidates[0][1]
        else:
            s = -1
            
        for k, v in candidates:
            if v != 1 and v == s:
                answer.append(k)

    answer.sort()

    return answer





print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))  # ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))  # ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))  # ["WX", "XY"]
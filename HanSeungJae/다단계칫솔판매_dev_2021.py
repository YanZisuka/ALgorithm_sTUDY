def solution(enroll, referral, seller, amount):
    answer = []
    tree = {}

    for i, e in enumerate(enroll):
        ref = referral[i]
        tree[e] = [ref, 0]
    
    for i, s in enumerate(seller):
        cash = amount[i] * 100
        fee = cash // 10
        tree[s][1] += (cash - fee)
        ref = tree[s][0]

        while ref != '-' and fee != 0:
            new_fee = fee // 10
            tree[ref][1] += fee - new_fee
            fee = new_fee
            ref = tree[ref][0]

    for v in tree.values():
        answer.append(v[1])
    
    return answer





print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
# [360, 958, 108, 0, 450, 18, 180, 1080]
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]))
# [0, 110, 378, 180, 270, 450, 0, 0]
def solution(n, k):
    def conv(n, k):
        res = ''
        while n // k != 0:
            res = str((n % k)) + res
            n = n // k
        res = str((n % k )) + res
        return res

    def check(num):
        if num == 1: return False
        n = 2
        while n <= (num) ** 0.5:
            if num % n == 0: return False
            n += 1
        return True

    answer = 0
    res = conv(n, k)
    cand = res.split('0')
    for c in cand:
        if not c: continue
        target = int(c)
        if check(target):
            answer += 1
            
    return answer





print(solution(437674, 3))
print(solution(110011, 10))
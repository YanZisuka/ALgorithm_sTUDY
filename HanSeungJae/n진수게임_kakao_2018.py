from string import ascii_uppercase

def solution(n, t, m, p):
    table = {
        i: str(i) for i in range(10)
    }
    for i in range(6):
        table[10 + i] = ascii_uppercase[i]

    def conv(n, num):
        st = '' if num else '0'
        while num:
            st = table.get(num % n) + st
            num //= n
        return st
    
    answer = ''
    nums = 'Z'

    for i in range(100000):
        nums += conv(n, i)

    turn = 1
    while len(answer) < t:
        if m != p and turn % m == p:
            answer += nums[turn]
        elif m == p and turn % m == 0:
            answer += nums[turn]
        turn += 1

    return answer





print(solution(2, 4, 2, 1))  # "0111"
print(solution(16, 16, 2, 1))  # "02468ACE11111111"
print(solution(16, 16, 2, 2))  # "13579BDF01234567"
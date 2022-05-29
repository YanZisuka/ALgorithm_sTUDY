def solution(p):

    def recursive(w):
        if not w: return ''

        c = True; cnt = 0
        for i, char in enumerate(w):
            if char == '(': cnt += 1
            elif char == ')': cnt -= 1
            if cnt < 0: c = False
            if cnt == 0:
                u, v = w[:i+1], w[i+1:]
                if c: return u + recursive(v)
                else: return '(' + recursive(v) + ')' + ''.join([')' if s == '(' else '(' for s in u[1:-1]])

    answer = recursive(p)

    return answer





print(solution("(()())()"))  # "(()())()"
print(solution(")("))  # "()"
print(solution("()))((()"))  # "()(())()"

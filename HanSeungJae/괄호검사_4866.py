import sys
sys.stdin = open('input.txt')


def check_bracket(codeline):
    stack = []
    for i in range(n):
        if codeline[i] == '(' or codeline[i] == '{':
            stack.append(codeline[i])
            
        elif codeline[i] == '}':
            if len(stack) == 0:
                return 0
            elif stack[-1] == '(':
                return 0
            elif stack[-1] == '{':
                stack.pop()
                
        elif codeline[i] == ')':
            if len(stack) == 0:
                return 0
            elif stack[-1] == '{':
                return 0
            elif stack[-1] == '(':
                stack.pop()
    if len(stack) == 0:
        return 1
    return 0


t = int(input())
for tc in range(1, t+1):
    codeline = input()
    n = len(codeline)
    
    print(f'#{tc} {check_bracket(codeline)}')
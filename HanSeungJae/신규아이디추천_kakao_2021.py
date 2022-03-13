from collections import deque

def solution(new_id):
    n = len(new_id)
    stack = deque()
    
    temp = new_id.lower()
    
    for i in range(n):
        if 97 <= ord(temp[i]) <= 122 or 48 <= ord(temp[i]) <= 57 or temp[i] == '-' or temp[i] == '_' or temp[i] == '.':
            stack.append(temp[i])
        if len(stack) > 1 and stack[-1] == '.' and stack[-2] == '.':
            stack.pop()
    
    
    if stack[0] == '.':
        stack.popleft()
    if len(stack) > 1:
        if stack[-1] == '.':
            stack.pop()
        
    if len(stack) == 0:
        stack.append('a')
    if len(stack) <= 2:
        while len(stack) < 3:
            stack.append(stack[-1])
    if len(stack) >= 16:
        tmp = deque()
        for i in range(15):
            tmp.append(stack[i])
        stack = tmp
    
    if stack[0] == '.':
        stack.popleft()
    if stack[-1] == '.':
        stack.pop()
        
    return ''.join(map(str, stack))
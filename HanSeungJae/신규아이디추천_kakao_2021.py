"""
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
"""

import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    new_id = new_id[1:] if new_id and new_id[0] == '.' else new_id
    new_id = new_id[:-1] if new_id and new_id[-1] == '.' else new_id
    new_id = 'a' if not new_id else new_id
    new_id = new_id[:15] if len(new_id) >= 16 else new_id
    new_id = new_id[:-1] if new_id and new_id[-1] == '.' else new_id
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id
import sys
sys.stdin = open('input.txt')


def solution():
    stack = [1, 3]
    while len(stack) < n//10:
        stack.append(stack[-1] + stack[-2] * 2)
    return stack[-1]


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    
    print(f'#{tc} {solution()}')
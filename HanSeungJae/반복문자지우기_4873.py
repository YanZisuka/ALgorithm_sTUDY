import sys
sys.stdin = open('input.txt')


def pop_duplicatedChar(string):
    stack = []
    for i in range(n):
        stack.append(string[i])
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    return stack


t = int(input())
for tc in range(1, t+1):
    string = input()
    n = len(string)
    
    print(f'#{tc} {len(pop_duplicatedChar(string))}')
            
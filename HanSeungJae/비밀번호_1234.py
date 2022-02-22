import sys
sys.stdin = open('input.txt')


def pop_duplicatedChar(string):
    stack = []
    for i in range(n):
        stack.append(string[i])
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    return ''.join(map(str, stack))


for tc in range(1, 11):
    n, string = input().split()
    n = int(n)

    print(f'#{tc} {pop_duplicatedChar(string)}')

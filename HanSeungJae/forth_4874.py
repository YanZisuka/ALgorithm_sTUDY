import sys
sys.stdin = open('input.txt')


def forth(codeline):
    stack = []
    for i in range(len(codeline)):
        if codeline[i] == '+':
            tmp = stack.pop()
            stack.append(stack.pop() + tmp)
        elif codeline[i] == '-':
            tmp = stack.pop()
            stack.append(stack.pop() - tmp)
        elif codeline[i] == '*':
            tmp = stack.pop()
            stack.append(stack.pop() * tmp)
        elif codeline[i] == '/':
            tmp = stack.pop()
            stack.append(stack.pop() // tmp)
        elif codeline[i] == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'
        else:
            stack.append(int(codeline[i]))


t = int(input())
for tc in range(1, t+1):
    codeline = input().split()
    
    try:
        print(f'#{tc} {forth(codeline)}')
    except IndexError:
        print(f'#{tc} error')
    except ValueError:
        print(f'#{tc} error')
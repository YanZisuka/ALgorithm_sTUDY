import sys
sys.stdin = open('input.txt')


def cut_stick(n, arr):
    stack = 0
    cut = 0
    i = 0
    while True:
        if i >= n:
            break
        if arr[i] == '(':
            if arr[i + 1] == ')':
                cut += stack
                i += 2
                continue
            else:
                stack += 1
        elif arr[i] == ')':
            stack -= 1
            cut += 1
        i += 1
    return cut


t = int(input())
for tc in range(1, t+1):
    arr = input()
    n = len(arr)
    
    print(f'#{tc} {cut_stick(n, arr)}')
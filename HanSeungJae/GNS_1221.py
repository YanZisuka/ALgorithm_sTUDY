import sys
sys.stdin = open('input.txt')


def encoding(n, string):
    for i in range(n):
        if string[i] == 0:
            string[i] = 'ZRO'
        elif string[i] == 1:
            string[i] = 'ONE'
        elif string[i] == 2:
            string[i] = 'TWO'
        elif string[i] == 3:
            string[i] = 'THR'
        elif string[i] == 4:
            string[i] = 'FOR'
        elif string[i] == 5:
            string[i] = 'FIV'
        elif string[i] == 6:
            string[i] = 'SIX'
        elif string[i] == 7:
            string[i] = 'SVN'
        elif string[i] == 8:
            string[i] = 'EGT'
        elif string[i] == 9:
            string[i] = 'NIN'
    return string

def decoding(n, string):
    for i in range(n):
        if string[i] == 'ZRO':
            string[i] = 0
        elif string[i] == 'ONE':
            string[i] = 1
        elif string[i] == 'TWO':
            string[i] = 2
        elif string[i] == 'THR':
            string[i] = 3
        elif string[i] == 'FOR':
            string[i] = 4
        elif string[i] == 'FIV':
            string[i] = 5
        elif string[i] == 'SIX':
            string[i] = 6
        elif string[i] == 'SVN':
            string[i] = 7
        elif string[i] == 'EGT':
            string[i] = 8
        elif string[i] == 'NIN':
            string[i] = 9
    return string


t = int(input())
for tc in range(1, t+1):
    n = int(input()[3:])
    string = input().split()
    arr = sorted(decoding(n, string))
    result = encoding(n, arr)
    
    print(f'#{tc}\n{" ".join(result)}')
    
    
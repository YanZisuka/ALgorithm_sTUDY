import sys
sys.stdin = open('input.txt')

nums = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}


def findMeaningfulCode(code):
    for i in range(n):
        if 1 in code[i]:
            code = code[i]
            break

    code = ''.join(map(str, code))

    for i in range(m - 1, -1, -1):
        if code[i] != '0':
            code = code[i - 55:i + 1]  # check
            break
            
    return code


def decode(code):
    for i in range(0, 50, 7):
        decode = code[i:i+7]
        if decode in nums.keys():
            key.append(nums[decode])
            
            
def check(key):
    global value
    global answer
    
    for i in range(8):
        if i % 2 == 0:
            value += key[i] * 3
        else:
            value += key[i]

    if value % 10 == 0:
        for i in range(8):
            answer += key[i]
    else:
        answer = 0
            

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    key = []
    value = 0
    answer = 0
    
    code = [list(map(int, input())) for _ in range(n)]
    code = findMeaningfulCode(code)
    decode(code)
    check(key)
    
    print(f'#{tc} {answer}')
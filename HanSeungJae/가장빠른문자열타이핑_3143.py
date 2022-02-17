import sys
sys.stdin = open('input.txt')


def cnt_typing_string(string, pattern):
    i = 0
    cnt = 0
    
    while True:
        cnt += 1
        if i == len(string)-1:
            return cnt
        if pattern == string[i:i+len(pattern)]:
            i += len(pattern)
            if i >= len(string)-1:
                return cnt
            continue
        i += 1


t = int(input())
for tc in range(1, t+1):
    string, pattern = input().split()
    
    print(f'#{tc} {cnt_typing_string(string, pattern)}')
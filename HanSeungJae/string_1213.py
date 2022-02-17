import sys
sys.stdin = open('input.txt', encoding='utf-8')

for tc in range(1, 11):
    n = int(input())
    pattern = input()
    string = input()
    cnt = 0
    
    for i in range(len(string)-len(pattern)+1):
        if pattern == string[i:i+len(pattern)]:
            cnt += 1
            
    print(f'#{tc} {cnt}')
    
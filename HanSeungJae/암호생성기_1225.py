from collections import deque
import sys
sys.stdin = open('input.txt')


def encode():
    queue = deque()
    for num in arr:
        queue.append(num)
    
    while True:
        if queue[-1] == 0:
            break
        for i in range(1, 6):
            num = queue.popleft()
            if num-i > 0:
                queue.append(num-i)
            else:
                queue.append(0)
                break
            
    return ' '.join(map(str, queue))
    
    
for tc in range(1, 11):
    t = int(input())
    arr = list(map(int, input().split()))
    
    print(f'#{tc} {encode()}')
    
    
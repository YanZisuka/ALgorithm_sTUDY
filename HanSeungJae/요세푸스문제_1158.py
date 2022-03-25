from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque()
answer = []
cnt = 0

for i in range(1, n+1):
    queue.append(i)

while queue:
    pick = queue.popleft()
    cnt += 1
    if cnt == k:
        answer.append(pick)
        cnt = 0
    else:
        queue.append(pick)
        
answer = ', '.join(map(str, answer))
print(f'<{answer}>')
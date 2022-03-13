import sys
input = sys.stdin.readline

n, h = map(int, input().split())
down = [0] * (h+1)  # 석순
up = [0] * (h+1)  # 종유석

minObstacle = float('inf')
numOfmin = 0

for i in range(n):
    if i % 2:
        down[int(input())] += 1
    else:
        up[int(input())] += 1

for i in range(h-1, 0, -1):
    down[i] += down[i+1]
    up[i] += up[i+1]

for i in range(1, h+1): 
    if minObstacle > (down[i] + up[h-i+1]):
        minObstacle = down[i] + up[h-i+1]
        numOfmin = 1
    elif minObstacle == (down[i] + up[h-i+1]):
        numOfmin += 1

print(minObstacle, numOfmin)

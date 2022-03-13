N, H = map(int,input().split())
bottom = []
top =[]

for _ in range(N//2):
    bottom.append(int(input()))
    top.append(int(input()))

cave = [0] * H

for height in range(H):
    for i in range(N//2):
        if bottom[i] >= height:
            cave[height] += 1
        if not H - top[i] >= height:
            cave[height] += 1

min = cave[0]
for height in range(H):
    if cave[height] < min:
        min = cave[height]

cnt = 0
for height in range(H):
    if cave[height] == min:
        cnt += 1

print(min, cnt)
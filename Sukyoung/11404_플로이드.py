import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
info = [[float('inf')] *(n+1)for _ in range(n+1)]
for _ in range(m):
    d,a,c = map(int,input().split())
    if c < info[d][a]:
        info[d][a] = c
for i in range(n+1):
    info[i][i] = 0

for transfer in range(1,n+1):
    for row in range(1,n+1):
        for col in range(1,n+1):
            if row != transfer and col != transfer:
                info[row][col] = min(info[row][col],info[row][transfer]+info[transfer][col])

for row in range(1,n+1):
    for col in range(1,n+1):
        if info[row][col] == float('inf'):
            print(0,end=' ')
        else:
            print(info[row][col],end=' ')
    print()

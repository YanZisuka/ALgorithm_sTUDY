import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
info = [[float('inf')] *(n+1)for _ in range(n+1)]  # 초기값 무한대로 설정
for _ in range(m):
    d,a,c = map(int,input().split())
    if c < info[d][a]:
        info[d][a] = c  # info[출발][도착] = 거리 삽입, 더 작은 값이 입력될 경우 갱신
for i in range(n+1):
    info[i][i] = 0  # 대각선 (출발,도착 노드 같은 경우) 0으로 설정

for transfer in range(1,n+1):  # matrix 순회하면서 특정 노드(transfer)거쳐서 갈 경우 거리 계산, 더 작은값으로 갱신
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

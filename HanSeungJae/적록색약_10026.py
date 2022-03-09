import copy, sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def dfs1(i, j, num):
    now_color = arr1[i][j]
    arr1[i][j] = num

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n:
            if arr1[ni][nj] == now_color:
                dfs1(ni, nj, num)


def dfs2(i, j, num):
    now_color = [arr2[i][j]]
    if now_color == ['R'] or now_color == ['G']:
        now_color = ['R', 'G']
    arr2[i][j] = num

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n:
            if arr2[ni][nj] in now_color:
                dfs2(ni, nj, num)


n = int(input())
arr1 = [list(input()) for _ in range(n)]
arr2 = copy.deepcopy(arr1)
cnt1 = 0
cnt2 = 0
k = 1

for i in range(n):
    for j in range(n):
        if arr1[i][j] == 'R' or arr1[i][j] == 'G' or arr1[i][j] == 'B':
            dfs1(i, j, k)
            k += 1
            cnt1 += 1
        if arr2[i][j] == 'R' or arr2[i][j] == 'G' or arr2[i][j] == 'B':
            dfs2(i, j, k)
            k += 1
            cnt2 += 1

print(cnt1, cnt2)
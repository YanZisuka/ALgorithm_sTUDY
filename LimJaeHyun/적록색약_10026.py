import sys
sys.setrecursionlimit(10000000)

N = int(input())

picture = list(list(input()) for _ in range(N))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# def normal_sight(i, j):
#     global cnt
#     if i < 0 or i >= N or j < 0 or j >= N:
#         return False
#     if picture[i][j] and not visited[i][j]:
#         cnt += 1
#         visited[i][j] = True
#         for k in range(4):
#             if 0 < i + dx[k] < N and 0 < j + dy[k] < N:
#                 if picture[i][j] == picture[i + dx[k]][j + dy[k]]:
#                     normal_sight(i + dx[k], j + dy[k])
#             else:
#                 continue
#         return True


def dfs(i, j):
    global cnt
    if i < 0 or j < 0 or i >= N or j >= N:
        return False
    if picture[i][j] and not visited[i][j]:
        cnt += 1
        visited[i][j] = True
        for k in range(4):
            if (0 <= i + dx[k] < N) and (0 <= j + dy[k] < N):
                if not visited[i + dx[k]][j + dy[k]]:
                    if picture[i + dx[k]][j + dy[k]] == picture[i][j]:
                        dfs(i + dx[k], j + dy[k])
        return True


# def color_blind(i, j):
#     global cnt
#     if i < 0 or i >= N or j < 0 or j >= N:
#         return False
#
#     if picture[i][j] == 'R' and not visited[i][j]:
#         cnt += 1
#         visited[i][j] = True
#         for k in range(4):
#             if 0 < i + dx[k] < N and 0 < j + dy[k] < N:
#                 if picture[i + dx[k]][j + dy[k]] == 'R' or picture[i + dx[k]][j + dy[k]] == 'G':
#                     cnt += 1
#                     color_blind(i + dx[k], j + dy[k])
#             else:
#                 continue
#         return True
#     elif picture[i][j] == 'G' and not visited[i][j]:
#         visited[i][j] = True
#         cnt += 1
#         for k in range(4):
#             if 0 < i + dx[k] < N and 0 < j + dy[k] < N:
#                 if picture[i + dx[k]][j + dy[k]] == 'R' or picture[i + dx[k]][j + dy[k]] == 'G':
#                     cnt += 1
#                     color_blind(i + dx[k], j + dy[k])
#             else:
#                 continue
#         return True
#     elif picture[i][j] == 'B' and not visited[i][j]:
#         visited[i][j] = True
#         cnt += 1
#         for k in range(4):
#             if 0 < i + dx[k] < N and 0 < j + dy[k] < N:
#                 if picture[i][j] == picture[i + dx[k]][j + dy[k]]:
#                     cnt += 1
#                     color_blind(i + dx[k], j + dy[k])
#             else:
#                 continue
#         return True
#
#

visited = [[0] * N for _ in range(N)]
cnt = 0
normal_color_zone = []
color_blind_zone = []

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            normal_color_zone.append(cnt)
        cnt = 0

for i in range(N):
    for j in range(N):
        if picture[i][j] == 'R':
            picture[i][j] = 'G'

visited = [[0] * N for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            color_blind_zone.append(cnt)
        cnt = 0

print(len(normal_color_zone), end=' ')
print(len(color_blind_zone))

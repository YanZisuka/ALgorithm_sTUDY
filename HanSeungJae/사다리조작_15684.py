import sys
input = sys.stdin.readline

def check():
    for start in range(n):
        k = start
        for j in range(h):
            if ladders[j][k]:
                k += 1
            elif k > 0 and ladders[j][k - 1]:
                k -= 1
        if k != start: return False
    return True


def dfs(cnt, x, y):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return

    for i in range(x, h):  # 가로로 탐색
        if i == x:
            k = y
        else:
            k = 0
        for j in range(k, n - 1):  # 세로로 탐색
            if not ladders[i][j] and not ladders[i][j+1]:
                if j > 0 and ladders[i][j - 1]:
                    continue
                ladders[i][j] = True
                dfs(cnt + 1, i, j + 2)  # 가로선 연속하지 않기 위해 세로선 2 증가
                ladders[i][j] = False

n, m, h = map(int, input().split())
ladders = [[False] * n for _ in range(h)]
if m == 0:
    print(0)
    exit(0)

for _ in range(m):
    a, b = map(int, input().split())
    ladders[a - 1][b - 1] = True
ans = 4
dfs(0, 0, 0)
print(ans if ans < 4 else -1)
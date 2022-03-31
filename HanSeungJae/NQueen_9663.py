"""
PyPy
"""
def dfs(i, j):
    global cnt

    if i == n-1:
        cnt += 1
        return

    col[j] = True
    dgn1[i-j] = True
    dgn2[i+j] = True

    ni = i + 1
    for nj in range(n):
        if not col[nj] and not dgn1[ni-nj] and not dgn2[ni+nj]:
            dfs(ni, nj)
            col[nj] = False
            dgn1[ni-nj] = False
            dgn2[ni+nj] = False


n = int(input())
cnt = 0

for j in range(n):
    col = [False] * n
    dgn1 = [False] * (2 * n - 1)
    dgn2 = [False] * (2 * n - 1)
    dfs(0, j)

print(cnt)
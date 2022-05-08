import sys
sys.setrecursionlimit(10**8)

def solution(info, edges):
    global answer

    def dfs(now, sheep, wolf, path):
        if tree[now][1] == 0:
            sheep += 1
        elif tree[now][1] == 1:
            wolf += 1

        if wolf and wolf >= sheep:
            return 0

        tmp_max = sheep

        for v in path:
            for nxt in tree[v][0]:
                if nxt not in path:
                    path += [nxt]
                    tmp_max = max(tmp_max, dfs(nxt, sheep, wolf, path))
                    path.pop()
        return tmp_max

    
    n = len(info)
    tree = [[[]] for _ in range(n)]

    for i in range(n):
        tree[i].append(info[i])

    for edge in edges:
        u, v = edge
        tree[u][0].append(v)
        tree[v][0].append(u)

    answer = dfs(0, 0, 0, [0])

    return answer





print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))  # 5
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))  # 5
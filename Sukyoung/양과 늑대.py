def solution(info, edges):
    global max_sheep
    max_sheep = 0
    tree = [[] for _ in range(len(info))]
    for e in edges:
        tree[e[0]].append(e[1])

    def dfs(x, sheep, wolf, linked):
        global max_sheep

        if info[x] == 0:  # 양인 경우
            sheep += 1
            max_sheep = max(max_sheep, sheep)
        else:
            wolf += 1  # 늑대인 경우

        if sheep <= wolf:  # 잡아먹히는 경우
            return

        linked += tree[x]
        for i in linked:
            dfs(i, sheep, wolf, linked=[link for link in linked if link != i])

    dfs(0, 0, 0, [])
    answer = max_sheep
    return answer
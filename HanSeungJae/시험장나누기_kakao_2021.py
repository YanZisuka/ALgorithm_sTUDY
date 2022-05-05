from itertools import combinations

def solution(k, num, links):

    def dfs(v):
        visited[v] = True
        dp[v] = num[v]

        for nxt in tree[v]:
            if not visited[nxt]:
                dfs(nxt)
                dp[v] += dp[nxt]

    answer = float('inf')
    n = len(links)
    tree = [[] for _ in range(n)]
    dp = [0] * n
    parents = [None] * n
    edges = []

    for i in range(n):
        link = links[i]
        l, r = link
        if l != -1:
            tree[l].append(i)
            tree[i].append(l)
            edges.append((i, l))
            parents[l] = i
        if r != -1:
            tree[r].append(i)
            tree[i].append(r)
            edges.append((i, r))
            parents[r] = i
    
    for i in range(n):
        if parents[i] == None:
            roots = [i]
    
    for cut in combinations(edges, k-1):
        visited = [False] * n
        tmp = 0

        for edge in cut:
            parent, child = edge
            tree[parent].remove(child)
            tree[child].remove(parent)
            roots.append(child)
        
        for root in roots:
            dfs(root)
            tmp = max(tmp, dp[root])
            
        answer = min(answer, tmp)
        roots = roots[:1]

        for edge in cut:
            parent, child = edge
            tree[parent].append(child)
            tree[child].append(parent)

    return answer
N, R, Q = map(int, input().split())
Tree = [[] for _ in range(N + 1)]
node_count = [0] * (N+1)
visited = [False for _ in range (N+1)]

for _ in range(N-1):
    U, V = map(int, input().split())
    Tree[U].append(V)
    Tree[V].append(U)


def dfs(r):
    node_count[r] = 1
    for node in Tree[r]:
        if node_count[node] == 0:
            dfs(node)
            node_count[r] += node_count[node]
    return


dfs(R)

print(node_count)

for _ in range(Q):
    q = int(input())
    print(node_count[q])


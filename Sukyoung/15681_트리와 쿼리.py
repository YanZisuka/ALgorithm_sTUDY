import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    visited[x] = 1
    for t in tree[x]:
        if visited[t] == 0:
            dfs(t)
            tree_cnt[x]+=tree_cnt[t]

N,R,Q = map(int,input().split())
tree = [[] for _ in range(N+1)]
visited = [0]*(N+1)
tree_cnt = [1]*(N+1) # 서브트리 정점의 개수

for i in range(N-1):
    U, V = map(int,input().split())
    tree[U].append(V)
    tree[V].append(U)

dfs(R)

for q in range(Q):
    num = int(input())
    print(tree_cnt[num])


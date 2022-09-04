import sys
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10 ** 8)


def inorder(node):
    lft, rght = tree[node][0], tree[node][1]
    if lft != -1:
        parents[lft] = node
        inorder(lft)
    inorder_res.append(node)
    if rght != -1:
        parents[rght] = node
        inorder(rght)


def pseudo_inorder(node):
    global cnt
    lft, rght = tree[node][0], tree[node][1]
    if lft != -1:
        pseudo_inorder(lft)
        cnt += 1
    if node == inorder_term:
        print(cnt)
        exit(0)
    cnt += 1
    if rght != -1:
        pseudo_inorder(rght)
        cnt += 1


n = int(input())
tree = [[] for _ in range(n+1)]
parents = [0] * (n+1)
inorder_res = []
for _ in range(n):
    a, b, c = map(int, input().split())
    tree[a].append(b)
    tree[a].append(c)


inorder(1)
inorder_term = inorder_res[-1]
cnt = 0
pseudo_inorder(1)
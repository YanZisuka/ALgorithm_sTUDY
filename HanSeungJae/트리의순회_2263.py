import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def preorder(inBegin, inEnd, postBegin, postEnd):
    if inBegin > inEnd or postBegin > postEnd:
        return

    root = postorder[postEnd]
    answer.append(root)

    left = position[root] - inBegin
    right = inEnd - position[root]

    preorder(inBegin, inBegin + left - 1, postBegin, postBegin + left - 1)
    preorder(inEnd - right + 1, inEnd, postEnd - right, postEnd - 1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0] * (n+1)
for i in range(n):
    position[inorder[i]] = i

answer = []

preorder(0, n-1, 0, n-1)

print(*answer)

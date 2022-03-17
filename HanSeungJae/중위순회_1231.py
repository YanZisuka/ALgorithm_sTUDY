import sys
sys.stdin = open('input.txt')


def setTree(input_str):
    node = int(input_str[0])
    value = input_str[1]

    tree[node] = value


def inorder_traverse(node):
    if 0 < node < n + 1:
        left = 2 * node
        right = 2 * node + 1
        
        if 0 < left < n + 1:
            inorder_traverse(left)
        answer.append(tree[node])
        if 0 < right < n + 1:
            inorder_traverse(right) 


for tc in range(1, 11):
    n = int(input())
    tree = [0] * (n+1)
    answer = []
    
    for i in range(n):
        input_str = input().split()
        setTree(input_str)
    
    inorder_traverse(1)
    print(f'#{tc} {"".join(answer)}')
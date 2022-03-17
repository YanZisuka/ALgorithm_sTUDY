from collections import deque
import sys
sys.stdin = open('input.txt')


def setTree(input_val):
    if len(input_val) == 4:
        num = int(input_val[0])
        val = input_val[1]
        left = int(input_val[2])
        right = int(input_val[3])

        tree[num][0] = val
        tree[num][1] = left
        tree[num][2] = right

    elif len(input_val) == 2:
        num = int(input_val[0])
        val = int(input_val[1])

        tree[num][0] = val
    
    
def postorder_traverse(node):
    if 0 < node < n+1:
        left = tree[node][1]
        right = tree[node][2]
        
        if left:
            postorder_traverse(left)
        if right:
            postorder_traverse(right)
        queue.append(tree[node][0])
        
        calculus()
        

def calculus():
    if type(queue[-1]) == str:
        calc = queue.pop()
        right = queue.pop()
        left = queue.pop()
            
        if calc == '+':
            queue.append(left + right)
            return
        elif calc == '-':
            queue.append(left - right)
            return
        elif calc == '*':
            queue.append(left * right)
            return
        elif calc == '/':
            queue.append(left / right)
            return


for tc in range(1, 11):
    n = int(input())
    tree = [[0, 0, 0] for _ in range(n+1)]
    queue = deque()
    for i in range(n):
        input_val = list(input().split())
        setTree(input_val)
        
    postorder_traverse(1)
            
    print(f'#{tc} {int(queue[0])}')
        
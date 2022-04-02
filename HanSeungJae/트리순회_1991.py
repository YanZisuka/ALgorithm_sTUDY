from string import ascii_uppercase
import sys
input = sys.stdin.readline


def preorder(node):
    l = tree[node][0]
    r = tree[node][1]
    ans.append(node)
    if l != '.':
        preorder(l)
    if r != '.':
        preorder(r)

    
def inorder(node):
    l = tree[node][0]
    r = tree[node][1]
    if l != '.':
        inorder(l)
    ans.append(node)
    if r != '.':
        inorder(r)
    

def postorder(node):
    l = tree[node][0]
    r = tree[node][1]
    if l != '.':
        postorder(l)
    if r != '.':
        postorder(r)
    ans.append(node)


n = int(input())
alpha = list(ascii_uppercase)
tree = {alpha[i]: [] for i in range(n)}

for i in range(n):
    v, l, r = input().strip().split()
    tree[v].append(l)
    tree[v].append(r)

for i in range(3):
    ans = []
    if i == 0:
        preorder('A')
    elif i == 1:
        inorder('A')
    elif i == 2:
        postorder('A')
    print(''.join(map(str, ans)))
        

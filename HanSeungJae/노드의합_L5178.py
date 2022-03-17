import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n, m, l = map(int, input().split())
    tree = [0] * (n+1)
    
    for i in range(m):
        leaf, val = map(int, input().split())
        tree[leaf] = val
        
    for i in range(n, 1, -1):
        tree[i//2] += tree[i]
        
    print(f'#{tc} {tree[l]}')
import sys
sys.stdin = open('input.txt')


def find(v):
    if parents[v] != v:
        parents[v] = find(parents[v])
    return parents[v]
    
    
def union(v1, v2):
    a = find(v1)
    b = find(v2)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def kruskal():
    global totalCost
    
    for i in range(e):
        a, b, c = edges[i]
        
        if find(a) != find(b):
            union(a, b)
            totalCost += c


t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    parents = [i for i in range(v+1)]
    edges = []
    totalCost = 0
    
    for _ in range(e):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        
    edges.sort(key=lambda x: x[2])
    
    kruskal()
        
    print(f'#{tc} {totalCost}')
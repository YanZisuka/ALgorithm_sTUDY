from math import *
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
    
    for i in range(len(edges)):
        a, b, c = edges[i]
        
        if find(a) != find(b):
            union(a, b)
            totalCost += c**2


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())
    parents = [i for i in range(n)]
    edges = []
    
    totalCost = 0
    for i in range(n-1):
        for j in range(i+1, n):
            cost = sqrt(abs(xs[i]-xs[j])**2 + abs(ys[i]-ys[j])**2)
            edges.append((i, j, cost))
            
    edges.sort(key=lambda x: x[2])
    
    kruskal()
    
    print(f'#{tc} {round(E * totalCost)}')
    
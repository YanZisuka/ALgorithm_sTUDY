from collections import deque
import sys
input = sys.stdin.readline

def topology_sort():
    queue = deque()
    for i in range(1,N+1):
        if indegree[i] == 0:
            queue.append(i)
            count[i][i]+=1  # 기본 부품에 필요한 부품 -> 자기 자신 1개

    while queue:
        element = queue.popleft()
        for e in info[element]:
            indegree[e[0]] -=1
            for c in range(1,N+1):
                count[e[0]][c] += (count[element][c]*e[1])  # 필요한 부품 개수 리스트 순회하며 업데이트
            if indegree[e[0]] == 0:
                queue.append(e[0])

N = int(input())
info = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
count=[[0]*(N+1) for _ in range(N+1)]  # 부품마다 필요한 부품 개수 리스트
M = int(input())
for i in range(1,M+1):
    m,b,c = map(int,input().split()) # 만들 부품, 필요한 부품, 개수
    info[b].append([m,c])
    indegree[m] +=1

topology_sort()

for idx,num in enumerate(count[N]):  # 마지막 부품(완제품)에 필요한 부품 개수 리스트
    if num != 0:  # 0개가 아닌 부품
        print(idx,num)



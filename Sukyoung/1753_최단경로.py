import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    queue = []
    heapq.heappush(queue,[0,start]) # heap에 담아서 최단 거리를 빨리 찾게 함
    final_distance[start] = 0

    while queue:
        distance,node = heapq.heappop(queue)
        if distance <= final_distance[node]:  # 탐색 한 적 없는 경로라면
            for i in info[node]:  # 탐색
                sum_distance = i[1]+distance  # 해당 위치까지의 거리 + 가중치
                if sum_distance < final_distance[i[0]]:  # 기존에 구한 거리보다 짧으면
                    final_distance[i[0]] = sum_distance  # 최단 거리 갱신
                    heapq.heappush(queue,[sum_distance,i[0]])  # queue에 삽입

V, E = map(int,input().split())
K = int(input())
info = [[] for _ in range(V+1)]
final_distance = [float('inf')]*(V+1)  # 초기값은 무한대로 설정

for i in range(E):
    u,v,w = map(int,input().split())
    info[u].append([v,w])   # [연결노드 , 가중치] 정보 삽입

dijkstra(K)

for i in range(1,V+1):
    if final_distance[i] == float('inf'):
        print('INF')
    else:
        print(final_distance[i])


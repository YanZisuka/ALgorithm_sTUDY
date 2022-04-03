import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):  # 다익스트라 함수 실행
    final_distance = [float('inf')] * (V + 1)
    queue = []
    heapq.heappush(queue,[0,start])
    final_distance[start] = 0

    while queue:
        distance,node = heapq.heappop(queue)
        if distance <= final_distance[node]:
            for i in info[node]:
                sum_distance = i[1]+distance
                if sum_distance < final_distance[i[0]]:
                    final_distance[i[0]] = sum_distance
                    heapq.heappush(queue,[sum_distance,i[0]])
    return final_distance

V, E = map(int,input().split())
info = [[] for _ in range(V+1)]


for i in range(E):
    u,v,w = map(int,input().split())  # 양방향 탐색이 가능하도록 시작,도착 노드 모두 탐색
    info[u].append([v,w])
    info[v].append([u,w])

v1,v2 = map(int,input().split())
result1 = 0
result2 = 0
start_1 = dijkstra(1)
start_v1 = dijkstra(v1)
start_v2 = dijkstra(v2)

# 1-v1-v2-V vs 1-v2-v1-V 중 더 짧은 거리 선택
result = min(start_1[v1]+start_v1[v2]+start_v2[V],start_1[v2]+start_v2[v1]+start_v1[V])
if result == float('inf'):
    print(-1)
else:
    print(result)
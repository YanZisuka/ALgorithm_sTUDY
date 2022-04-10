import heapq
import sys
input = sys.stdin.readline

def fox(start): # 여우의 최단 거리 - 기존 다익스트라
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
def wolf(start): #늑대의 최단 거리 - 기존 다익스트라
    queue = []
    heapq.heappush(queue,[0,start])


    final_distance[start] = 0

    while queue1:
        distance,node = heapq.heappop(queue1)
        if distance <= final_distance[node]:
            for i in info[node]:
                sum_distance = i[1]+distance
                if sum_distance < final_distance[i[0]]:
                    final_distance[i[0]] = sum_distance
                    heapq.heappush(queue1,[sum_distance,i[0]])
V, E = map(int,input().split())
info = [[] for _ in range(V+1)]
final_distance = [float('inf')]*(V+1)

for i in range(E):
    u,v,w = map(int,input().split())
    info[u].append([v,w])

fox(1)
print(info)
print(final_distance)

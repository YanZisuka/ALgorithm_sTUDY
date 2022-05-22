from heapq import *

def solution(n, s, a, b, fares):
    INF = float('inf')

    def dijkstra(s):
        dist = [[INF, []]] * (n+1)
        dist[s] = [0, [s]]
        pq = []
        heappush(pq, (dist[s][0], s, dist[s][1]))

        while pq:
            dst, now, path = heappop(pq)

            if dist[now][0] < dst: continue

            for nxt, weight in graph[now]:
                shortest = dist[now][0] + weight
                if shortest < dist[nxt][0]:
                    dist[nxt] = [shortest, path + [nxt]]
                    heappush(pq, (shortest, nxt, path + [nxt]))
        return dist


    graph = [[] for _ in range(n+1)]
    for fare in fares:
        u, v, c = fare
        graph[u].append((v, c))
        graph[v].append((u, c))

    dist = dijkstra(s)
    answer = dist[a][0] + dist[b][0]

    md = [i for i in range(1, n+1) if i != s]
    for m in md:
        d1 = dijkstra(s)[m][0]
        d2 = dijkstra(m)
        answer = min(answer, d1 + d2[a][0] + d2[b][0])

    return answer





print(solution(6, 4, 6, 2, 	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))  # 82
print(solution(7, 3, 4, 1, 	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))  # 14
print(solution(6, 4, 5, 6, 		[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))  # 18
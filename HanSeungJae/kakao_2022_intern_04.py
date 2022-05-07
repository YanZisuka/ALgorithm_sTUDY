from heapq import *


def solution(n, paths, gates, summits):

    def dijkstra(s, e):
        dist = [float('inf')] * (n+1)
        pq = []
        dist[s] = 0
        heappush(pq, (0, s))

        while pq:
            intensity, now = heappop(pq)

            if now == e: return dist
            
            if dist[now] < intensity:
                continue

            for nxt, weight in graph[now]:
                tmp_intensity = max(intensity, weight)
                if tmp_intensity < dist[nxt]:
                    dist[nxt] = tmp_intensity
                    if nxt not in summits and nxt not in gates:
                        heappush(pq, (tmp_intensity, nxt))
        return dist

    graph = [[] for _ in range(n+1)]
    for path in paths:
        i, j, w = path
        graph[i].append((j, w))
        graph[j].append((i, w))

    answer = []
    min_intensity = float('inf')

    for gate in gates:
        g_weights = []
        for nxt, weight in graph[gate]:
            g_weights.append(weight)
        if min(g_weights) > min_intensity: continue

        for summit in summits:
            s_weights = []
            for prev, weight in graph[summit]:
                s_weights.append(weight)
            if min(s_weights) > min_intensity: continue

            up_path = dijkstra(gate, summit)
            tmp_intensity = up_path[summit]
            if tmp_intensity > min_intensity: continue

            if tmp_intensity <= min_intensity:
                min_intensity = tmp_intensity
                answer.append([summit, tmp_intensity])

    answer.sort(key=lambda x: (x[1], x[0]))

    return answer[0]




print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))
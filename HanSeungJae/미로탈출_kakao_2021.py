from heapq import *


def solution(n, start, end, roads, traps):

    def dijkstra(s):
        pq = []
        heappush(pq, (0, s, 0))

        while pq:
            dst, now, state = heappop(pq)

            if now == end: return dst
            if visited[state][now] == True: continue
            else: visited[state][now] = True

            for nxt, weight, type in graph[now]:
                nxt_state = state
                now_is_trap = 1 if now in trap_dict else 0
                nxt_is_trap = 1 if nxt in trap_dict else 0

                if now_is_trap == 0 and nxt_is_trap == 0:
                    if type == 1: continue
                elif (now_is_trap + nxt_is_trap) == 1:
                    node = now if now_is_trap == 1 else nxt
                    now_trap_on = (state & (1<<trap_dict[node]))>>trap_dict[node]
                    if now_trap_on != type: continue
                else:
                    now_trap_on = (state & (1<<trap_dict[now]))>>trap_dict[now]
                    nxt_trap_on = (state & (1<<trap_dict[nxt]))>>trap_dict[nxt]
                    if (now_trap_on ^ nxt_trap_on) != type: continue

                if nxt_is_trap == 1:
                    nxt_state = state ^ (1<<trap_dict[nxt])

                heappush(pq, (dst+weight, nxt, nxt_state))
                

    graph = [[] for _ in range(n+1)]
    trap_dict = {trap: idx for idx, trap in enumerate(traps)}
    visited = [[False] * (n+1) for _ in range(1<<len(traps))]

    for i in range(len(roads)):
        p, q, s = roads[i]
        graph[p].append((q, s, 0))
        graph[q].append((p, s, 1))

    answer = dijkstra(start)

    return answer


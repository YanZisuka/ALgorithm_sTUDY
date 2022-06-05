from itertools import permutations


def solution(n, weak, dist):

    def DFS(n, weak, dist, cnt):
        global answer
        if not weak:
            answer = cnt
            return
        if not dist or cnt >= answer:
            return
        sub_dist = dist[:]
        d = sub_dist.pop()
        sub_weak_list = []
        for start_point in weak:
            sub_weak = weak[:]
            for i in range(len(weak)-1, -1, -1):
                if (sub_weak[i] - start_point) % n <= d:
                    sub_weak.pop(i)
            DFS(n, sub_weak, sub_dist, cnt + 1)
            sub_weak_list.append(sub_weak)
        sub_weak_list.sort(key=lambda x: len(x))
        for sw in sub_weak_list:
            if len(sw) == len(sub_weak_list[0]):
                DFS(n, sw, sub_dist, cnt + 1)
            else:
                break

    dist.sort()
    DFS(n, weak, dist, 0)

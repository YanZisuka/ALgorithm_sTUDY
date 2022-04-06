from collections import deque
import sys
input = sys.stdin.readline

def topology_sort():
    queue = deque()
    for i in range(1,N+1):  # 먼저 지어야하는 건물이 없는 건물 queue삽입
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        building = queue.popleft()
        time[building]+=pre_time[building]  # 사전에 소요된 시간 + 건축 시간

        for b in line_info[building]:
            if time[building]>pre_time[b]:  # 사전 소요 시간 최대값으로 갱신
                pre_time[b] = time[building]
            indegree[b]-=1
            if indegree[b] == 0:
                queue.append(b)


N = int(input())
time = [0]*(N+1)  # 건축에 걸리는 시간
pre_time=[0]*(N+1)  # 건축 전 먼저 지어야하는 건물에 소요되는 시간 저장 (사전 소요 시간)
indegree = [0]*(N+1)  # 먼저 지어야하는 건물 수 저장
line_info=[[] for _ in range(N+1)]  # 순서 정보
for i in range(1,N+1):
    info_list = list(map(int,input().split()))
    time[i] = info_list[0]
    for j in info_list[1:-1]:
        line_info[j].append(i)
        indegree[i]+=1
topology_sort()

for t in range(1,N+1):
    print(time[t])
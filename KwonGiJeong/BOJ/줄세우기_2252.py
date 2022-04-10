import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
inDegree = [0] * (N + 1)  # 진입 차수
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)  # a의 인덱스에 b를 넣고
    inDegree[B] += 1  # b의 진입 차수 +1

# 위상정렬 알고리즘
queue = deque()  # 큐
for shorty in range(1, N + 1):
    if inDegree[shorty] == 0:  # 진입 차수가 0인 쪼꼬미들 먼저 queue에 넣기
        queue.append(shorty)
line = []  # 줄 세울 곳
while queue :
    low_man = queue.popleft()
    line.append(str(low_man)) #  작은 애들 줄부터 세우고
    for high_man in graph[low_man]:  #  작은 애랑 비교했던 큰 애들
        inDegree[high_man] -= 1  #  진입차수로 지목 당했으니 차수 하나 제거
        if inDegree[high_man] == 0:  #  차수 제거해서 이제 지목 당할 일 없으면 차례가 온 것! (나보다 키 작았던 애들은 다 append 됐다!)
            queue.append(high_man)

answer = ' '.join(line)
print(answer)


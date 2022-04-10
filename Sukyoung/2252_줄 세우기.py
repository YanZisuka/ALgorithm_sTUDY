from collections import deque
import sys
input = sys.stdin.readline

# 위상정렬함수
def topology_sort(line_info,indegree):
    result = []  # 키 순서 리스트
    queue = deque()

    for i in range(1,N+1):  # 자기보다 작은 학생이 없는 학생(제일 작은 학생) queue에 삽입
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        student = queue.popleft()
        result.append(student)  # 키 순서 리스트 삽입
        for s in line_info[student]:  # 해당 학생과 키를 비교한 학생들 탐색
            indegree[s]-=1
            if indegree[s] == 0:  # 남은 학생 중 제일 작은 학생 queue 삽입
                queue.append(s)

    return result



# 입력받기
N,M = map(int,input().split())
line_info = [[] for _ in range(N+1)] # 간선 정보 받는 matrix(키 비교 결과)
indegree = [0] * (N+1) # 그래프 진입 차수 받기 (자기보다 작은 학생의 수)
result = []
for i in range(M):
    s,t = map(int,input().split())
    line_info[s].append(t)
    indegree[t]+=1

answer = topology_sort(line_info,indegree)
for a in answer:
    print(a,end=' ')
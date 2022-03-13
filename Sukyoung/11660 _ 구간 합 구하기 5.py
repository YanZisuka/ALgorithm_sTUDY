N, M = map(int,input().split())
zero= [[0]*(N+1)]
mat = zero + [[0]+list(map(int,input().split())) for _ in range(N)]  # mat 0행이랑 0열에 0 넣어줌

for i in range(1,N+1):  # mat 누적합으로 채움, 중복된 부분 빼주기
    for j in range(1,N+1):
        mat[i][j] += (mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1])

answer = []
for i in range(M):  # (x1,y1) 에서 (x2,y2)까지 합, 중복된 부분 더해주기
    x1, y1, x2, y2 = map(int,input().split())
    answer.append(mat[x2][y2] - mat[x2][y1-1] - mat[x1-1][y2] + mat[x1-1][y1-1])

#위에 for문에서 바로 print하면 출력이 바로바로 안됨 - 왜그런지 모르겠다...
# 그래서 append하고 하나씩 출력함
for num in answer:
    print(num)


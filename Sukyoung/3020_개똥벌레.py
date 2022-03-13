N, H = map(int,input().split())
top =[]  # 종유석
bottom=[]  # 석순
for j in range(N):
    if (j % 2) == 0: # 짝수는 석순
        bottom.append(int(input()))
    else:  # 홀수는 종유석
        top.append(int(input()))
top.sort()
bottom.sort()

def b_search(array,target):  # 이진탐색
    start = 0
    end = len(array)-1
    while start <= end:
       mid = (start+end)//2
       if target > array[mid]:
           start = mid+1
       else:
            end = mid-1
    return start

result = [0]*H
for i in range(1,H+1):
    result[i-1]+= N//2-b_search(top,H-i+1)  # 정렬했으니까 한번 부딪히기 시작하면 뒤에 종유석(석순)은 다 부딪힘
    result[i-1] += N//2-b_search(bottom,i)  # 전체에서 부딪히는 시작점 뺴서 부딪히는 석순(종유석)들의 개수 구함

print(min(result),result.count(min(result)))














"""
cave =[[0]*(N+1) for _ in range(H)]
for j in range(1,N+1):
    num = int(input())
    for i in range(H):
       if (j%2) == 0:
            if i in range(H-num,H):
                cave[i][j] += 1 + cave[i][j-1]
            else:
                cave[i][j] += cave[i][j-1]

       else:
            if i in range(num):
                cave[i][j] = 1 + cave[i][j-1]
            else:
                cave[i][j] += cave[i][j - 1]


result = []
for c in cave:
    result.append(c[N])
print(min(result),result.count(min(result)))


"""
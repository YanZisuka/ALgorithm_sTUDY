N = int(input())
array = list(map(int,input().split()))
cnt = [1]* N
for i in range(N):
    maxnum = 0
    for j in range(i): # 자기위치 전까지 숫자들 탐색
        if array[j]<array[i]: # 자기보다 작은 숫자 중
            if cnt[j]>=maxnum:  # 증가하는 수열 크기가 가장 큰 것
                maxnum = cnt[j]
            cnt[i] = maxnum + 1

print(max(cnt))

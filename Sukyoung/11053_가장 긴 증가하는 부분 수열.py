N = int(input())
array = list(map(int,input().split()))
cnt = [1]* N
for i in range(N):
    maxnum = 0
    for j in range(i):
        if array[j]<array[i]:
            if cnt[j]>=maxnum:
                maxnum = cnt[j]
            cnt[i] = maxnum + 1

print(max(cnt))

import sys
input = sys.stdin.readline


def recursive(idx, cnt1, cnt2, sum1, sum2):
    global curMin
    if idx == n:
        if cnt1 == cnt2:
            curMin = min(curMin, abs(sum1 - sum2))
        return

    check[idx] = True
    temp = 0
    for i in range(idx):
        if check[i] == True:
            temp += stat_list[i][idx] + stat_list[idx][i]
    recursive(idx+1, cnt1+1, cnt2, sum1+temp, sum2)

    check[idx] = False
    temp = 0
    for i in range(idx):
        if check[i] == False:
            temp += stat_list[i][idx] + stat_list[idx][i]
    recursive(idx+1, cnt1, cnt2+1, sum1, sum2+temp)


n = int(input())
stat_list = []
for _ in range(n):
    stats = list(map(int, input().split()))
    stat_list.append(stats)
check = [False] * n
curMin = 10000000

recursive(0, 0, 0, 0, 0)
print(curMin)
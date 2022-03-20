import sys
input = sys.stdin.readline

def dfs(start_list):
    global result

    for i in start_list:
        result.append(i[1])

        if dict[i[0]]:
            dfs(dict[i[0]])
            result.pop()

        elif not dict[i[0]]:
            sum = 0
            for i in range(len(result)-1,-1,-1):
                if result[i] > 0:
                    k = i
                    break
            for j in range(k,-1,-1):
                sum += result[j]
                num = sum - result[j]

                if sum < 0:
                    sum = 0
                if result[j] < 0:
                    result[j] += num
                    if result[j] > 0:
                        result[j] = 0
                elif result[j] > 0:
                    result[j] = 0
            sum_list.append(sum)
            result.pop()

N = int(input())
information = [[1,'S',0,0]]
for i in range(2,N+1):
    island = input().split()
    information.append([i,island[0],island[1],island[2]])

for info in information:
    if info[1] == 'S':
        info[2] = int(info[2])
    else:
        info[2] = -1 * int(info[2])

dict = {}
for i in range(N+1):
    list_ = []
    for info in information:
        if i == int(info[3]):
            list_.append([info[0],info[2]])
    dict[i] = list_

result =[]
sum_list=[]
dfs(dict[0])
print(sum(sum_list))


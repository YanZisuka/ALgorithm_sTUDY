def dfs(start_list):
    global result

    for i in start_list:
        result.append(i[1])
        print(result)

        if dict[i[0]]:
            dfs(dict[i[0]])
            result.pop()

        else:
            result_list.append(result)
            result.pop()
            print('k')
            print(result_list)






N = int(input())
information = []
for i in range(2,N+1):
    island = input().split()
    information.append([i,island[0],island[1],island[2]])
print(information)
for info in information:
    if info[1] == 'S':
        info[2] = int(info[2])
    else:
        info[2] = -1 * int(info[2])

dict = {}
for i in range(1,N+1):
    list_ = []
    for info in information:
        if i == int(info[3]):
            list_.append([info[0],info[2]])
    dict[i] = list_
print(dict)
result =[]
result_list=[]
dfs(dict[1])
# answer=[i for i in dfs(dict[1]) if i > 0]
print(result_list)
#print(sum(answer))


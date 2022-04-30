N, M = map(int,input().split())
value_list = [0,]
for i in range(N):
    value = int(input())
    value_acc = value_list[-1] + value
    value_list.append(value_acc)

min_value = 0
max_value = 0
for i in range(M-1,N):
    min_value = min(min_value,value_list[i-M+1])
    max_value = max(max_value,value_list[i+1] - min_value)
print(max_value)

# 구간 나눠서 최대 최소 구하면 20%만 맞음 - for문으로 범위를 다 돌려줘야함
# max_value = max(value_list[M-1:])
# max_index = value_list.index(max_value)
# print(max_index)
# min_value = 0
# if value_list[0:max_index-M+1]:
#     min_value = min(0,min(value_list[0:max_index-M+1]))
# print(max_value - min_value)

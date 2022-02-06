from itertools import permutations


def max_gab(lists):
    max = 0
    for i in lists:
        temp_max = 0
        for j in range(len(i)-1):
            temp_max += abs(i[j] - i[j+1])
        if max <= temp_max:
            max = temp_max
    return max

N = input()
numbers = input()
lists = list(permutations(numbers))
result = max_gab(lists)
print(result)





######## 헛짓거리 #########

# import copy

# def first_num(numbers): 
#     max = numbers[0]
#     min = numbers[0]
#     for i in range(len(numbers)):
#         if max <= numbers[i]:
#             max = numbers[i]
#     for j in range(len(numbers)):
#         if min >= numbers[j]:
#             min = numbers[j]

#     numbers.remove(max)
#     numbers.remove(min)
#     next_max = numbers[0]
#     next_min = numbers[0]
#     for i in range(len(numbers)):
#         if next_max <= numbers[i]:
#             next_max = numbers[i]
#     for j in range(len(numbers)):
#         if next_min >= numbers[j]:
#             next_min = numbers[j]
    
#     top_gab = abs(max - next_max)
#     bottom_gab = abs(next_min - min)
#     if top_gab >= bottom_gab:
#         return (min, False)
#     elif top_gab < bottom_gab:
#         return (max, True)

# def max_gap(numbers, start_num, max_or_min):
#     if len(numbers) == 2:
#         result_gab = abs(numbers[0]-numbers[1])
#         numbers.remove(start_num)
#         return (result_gab, numbers, None, None)
    
#     if max_or_min == True:
#         max = start_num
#         min = numbers[0]
#         for i in range(len(numbers)):
#             if min >= numbers[i]:
#                 min = numbers[i]
#                 nxt = min
#         max_or_min = False

#     elif max_or_min == False:
#         max = numbers[0]
#         min = start_num
#         for i in range(len(numbers)):
#             if max <= numbers[i]:
#                 max = numbers[i]
#                 nxt = max
#         max_or_min = True

#     result_gab = abs(max - min)
#     numbers.remove(start_num)
#     start_num = nxt

#     return (result_gab, numbers, start_num, max_or_min)

# numbers = [20, 1, 15, 8, 4, 10]
# temp_num = copy.deepcopy(numbers)
# first_step = first_num(temp_num)
# start_num = first_step[0]
# max_or_min = first_step[1]
# result = 0

# for j in range(len(numbers)-1):
#     temp = max_gap(numbers, start_num, max_or_min)
#     result += temp[0]
#     numbers = temp[1]
#     start_num = temp[2]
#     max_or_min = temp[3]

# print(result)
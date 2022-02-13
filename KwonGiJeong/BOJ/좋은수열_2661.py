### mission을 잘못 이해한 예 ###
# def is_good_list(numbers):
#     max_scope = len(numbers)//2
#     for scope in range(1, max_scope+1):
#         for i in range(len(numbers)-(scope*2)):
#             front_part = numbers[i:i+scope]
#             next_part = numbers[i+scope:i+(2*scope)]
#             print(front_part, next_part)
#             if front_part == next_part:
#                 return False
#     return True


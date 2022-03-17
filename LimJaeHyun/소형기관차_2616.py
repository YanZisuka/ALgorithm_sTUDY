N = int(input())
train = list(map(int, input().split()))
max_tow = int(input())
sum_val = 0
prefix_sum = [0]

for car in train:
    sum_val += car
    prefix_sum.append(sum_val)

combinations = []
for i in range(max_tow, len(train) + 1):
    combinations.append(prefix_sum[i] - prefix_sum[i - max_tow])

max_combination = [combinations[0]]
for idx in range(1, len(combinations)):

    # if len(max_combination) < 3:
    #     max_combination.append(combinations[idx])
    # elif len(max_combination) == 3 and combinations[idx] > min(max_combination) and combinations[idx] not in max_combination:
    #     if combinations[idx - 1] not in max_combination:
    #         max_combination.remove(min(max_combination))
    #         max_combination.append(combinations[idx])

print(sum(max_combination))

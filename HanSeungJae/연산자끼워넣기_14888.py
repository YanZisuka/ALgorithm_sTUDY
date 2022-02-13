from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
plus_cnt, minus_cnt, product_cnt, div_cnt = map(int, input().split())
results = []
factors = []
for _ in range(plus_cnt):
    factors.append('+')
for _ in range(minus_cnt):
    factors.append('-')
for _ in range(product_cnt):
    factors.append('*')
for _ in range(div_cnt):
    factors.append('/')
permutation_list = list(set(permutations(factors, len(factors))))  # 중복되는 순열조합 제거

for i in range(len(permutation_list)):
    total_val = arr[0]
    for j in range(len(permutation_list[i])):
        if permutation_list[i][j] == '+':
            total_val += arr[j+1]
        if permutation_list[i][j] == '-':
            total_val -= arr[j+1]
        if permutation_list[i][j] == '*':
            total_val *= arr[j+1]
        if permutation_list[i][j] == '/':
            if total_val < 0:
                total_val = -total_val
                total_val //= arr[j+1]
                total_val = -total_val
                continue
            total_val //= arr[j+1]
    results.append(total_val)

print(max(results))
print(min(results))

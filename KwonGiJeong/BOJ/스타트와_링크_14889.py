from itertools import combinations

n = int(input())
array = [i for i in range(n)]
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
result = float('inf')
for start_samples in combinations(array, n//2):
    start_stat = 0
    link_stat = 0
    link_samples = list(set(array) - set(start_samples))
    for stat in combinations(start_samples, 2):
        start_stat += matrix[stat[0]][stat[1]]
        start_stat += matrix[stat[1]][stat[0]]
    for stat in combinations(link_samples, 2):
        link_stat += matrix[stat[0]][stat[1]]
        link_stat += matrix[stat[1]][stat[0]]
    result = min(result, abs(start_stat-link_stat))
print(result)
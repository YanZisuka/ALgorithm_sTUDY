from itertools import permutations

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

answers = list(permutations(arr, m))

for answer in answers:
    answer = ' '.join(map(str, list(answer)))
    print(f'{answer}')

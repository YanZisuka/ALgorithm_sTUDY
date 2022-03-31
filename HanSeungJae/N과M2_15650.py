from itertools import permutations

n, m = map(int, input().split())
arr = [i+1 for i in range(n)]
answers = set()

for case in permutations(arr, m):
    case = list(case)
    case.sort()
    answers.add(tuple(case))

answers = list(answers)
answers.sort()

for answer in answers:
    print(' '.join(map(str, answer)))

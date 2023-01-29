import sys

input = lambda: sys.stdin.readline().strip()


def get_gradient(fr, to):
    return (heights[fr] - heights[to]) / (fr - to)


n = int(input())
heights = [-1] + list(map(int, input().split()))
answers = [-1] + [0] * n

for i, _h in enumerate(heights):
    if i == 0:
        continue

    cnts = [0, 0]

    max_grad = None
    for x in range(i + 1, n + 1):
        grad = get_gradient(i, x)
        if max_grad == None or grad > max_grad:
            max_grad = grad
            cnts[0] += 1

    min_grad = None
    for x in range(i - 1, 0, -1):
        grad = get_gradient(i, x)
        if min_grad == None or grad < min_grad:
            min_grad = grad
            cnts[1] += 1

    answers[i] = sum(cnts)

print(max(answers))

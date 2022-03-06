import sys

sys.stdin = open('input_16437.txt')


def come(now):
    temp_sheeps = sheeps[now]

    for prev in tree[now]:
        temp_sheeps += come(prev)

    if wolves[now] != 0:
        if temp_sheeps < wolves[now]:
            wolves[now] -= temp_sheeps
            temp_sheeps = 0
        else:
            temp_sheeps -= wolves[now]
            wolves[now] = 0

    return temp_sheeps

N = int(input())

wolves = [0 for _ in range(N)]
sheeps = [0 for _ in range(N)]
tree = [[] for _ in range(N)]

for i in range(1, N):
    t, a, p = input().split()
    a = int(a)
    p = int(p) - 1
    if t == "W":
        wolves[i] = a
    else:
        sheeps[i] = a
    tree[p].append(i)

print(come(0))
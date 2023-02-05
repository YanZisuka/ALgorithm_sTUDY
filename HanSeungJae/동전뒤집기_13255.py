import sys

input = lambda: sys.stdin.readline().strip()

total = int(input())
k = int(input())
arr = list(map(int, input().split()))

head = total
for flip in arr:
    exp_head = head * (1 - flip / total)
    head = exp_head + (total - head) * (flip / total)

print(head)

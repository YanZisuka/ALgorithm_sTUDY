import sys
input = sys.stdin.readline


def binarySearch(target):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if cards[mid] == target:
            return 1
        elif cards[mid] < target:
            start = mid + 1
        elif cards[mid] > target:
            end = mid - 1
    return 0


n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
targets = list(map(int, input().split()))
answer = []

for target in targets:
    answer.append(binarySearch(target))

print(*answer)
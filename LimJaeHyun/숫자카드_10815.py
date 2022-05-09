def binary_search(target, data):
    start_idx = 0
    end_idx = len(data) - 1

    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2

        if data[mid_idx] == target:
            return True
        elif data[mid_idx] < target:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx - 1
    return False


N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
search = list(map(int, input().split()))

answer = []
for query in search:
    if binary_search(query, cards):
        answer.append(1)
    else:
        answer.append(0)
print(*answer)

# for query in search:
#     if query in cards:
#         answer.append(1)
#     else:
#         answer.append(0)
# print(*answer)


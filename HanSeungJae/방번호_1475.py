import sys
def input(): return sys.stdin.readline().strip()


n = input()
arr = [0] * 10

for char in n:
    arr[int(char)] += 1

while arr[6] != arr[9]:
    if abs(arr[9] - arr[6]) < 2:
        break

    if arr[9] > arr[6]:
        arr[9] -= 1
        arr[6] += 1
    else:
        arr[9] += 1
        arr[6] -= 1

print(max(arr))

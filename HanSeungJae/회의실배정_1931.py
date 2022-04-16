import sys
input = sys.stdin.readline


n = int(input())
arr = []
for i in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))

arr.sort(key=lambda x: (x[1], x[0]))

answer = [arr[0]]

for i in range(1, n):
    if arr[i][0] >= answer[-1][1]:
        answer.append(arr[i])

print(len(answer))
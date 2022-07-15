import sys
input = lambda: sys.stdin.readline().strip()


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = 0
a.sort()
b.sort(reverse=True)

for i in range(n):
    answer += a[i] * b[i]

print(answer)
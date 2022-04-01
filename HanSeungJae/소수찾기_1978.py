def isprime(num):
    k = 2

    if num <= 1:
        return False

    while k ** 2 <= num:
        if num % k == 0:
            return False
        k += 1
    return True


n = int(input())
arr = list(map(int, input().split()))
ans = 0

for num in arr:
    if isprime(num):
        ans += 1

print(ans)
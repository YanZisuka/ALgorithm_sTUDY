import sys
input = lambda: sys.stdin.readline().strip()


tc = int(input())
for _ in range(tc):
    hash_a, hash_b = {}, {}
    a, b = input().split()
    flag = False

    for char in a:
        if hash_a.get(char): hash_a[char] += 1
        else: hash_a[char] = 1
    for char in b:
        if hash_b.get(char): hash_b[char] += 1
        else: hash_b[char] = 1

    for k, v in hash_a.items():
        if hash_b.get(k) and hash_b[k] == v: continue
        print('Impossible')
        flag = True
        break
    if not flag: print('Possible')
    
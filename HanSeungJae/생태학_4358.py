import sys
input = lambda: sys.stdin.readline().strip()


total = 0
table = {}

while True:
    tree = input()
    if not tree: break
    total += 1
    if table.get(tree):
        table[tree] += 1
    else:
        table[tree] = 1

keys = list(table.keys())
keys.sort()
for k in keys:
    print(f'{k} {((table[k] / total) * 100):.4f}')

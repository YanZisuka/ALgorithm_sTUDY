def hanoi(n, _from=1, to=3):
    if n == 1:
        print(f'{_from} {to}')
    else:
        empty = 6-_from-to
        hanoi(n-1, _from, empty)
        print(f'{_from} {to}')
        hanoi(n-1, empty, to)

n = int(input())
print(2**n-1)
hanoi(n)
from unittest.mock import patch


def stars(n):
    if n == 3:
        return ['***','* *','***']
    else:
        arr = []
        for i in range(n):
            if i // len(stars(n//3)) == 1:
                arr.append(stars(n//3)[i%len(stars(n//3))] + ' '*(n//3) + stars(n//3)[i%len(stars(n//3))])
            else:
                arr.append(stars(n//3)[i%len(stars(n//3))]*3)
        return arr

n = int(input())

print('\n'.join(stars(n)))

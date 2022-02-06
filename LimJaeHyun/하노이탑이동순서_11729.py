n = int(input())

def saigon_tear(n, start, middle, end):
    if n == 1:
        print(start, end)
    else:
        # saigon_tear(n - 1, start, end, middle)
        # print(start, end)
        # saigon_tear(n - 1, middle, start, end) 추가 공부 필요

total = 2**n - 1
print(total)

saigon_tear(n, 1, 2, 3)

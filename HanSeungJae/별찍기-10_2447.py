import sys
input = sys.stdin.readline

# def stars(n):  # 완벽하게 재귀로만 구성했지만 시간복잡도가 O(n^2) 이상이므로 백준에 채점하면 시간초과가 뜬다 ㅠㅠ
#     if n == 3:
#         return ['***','* *','***']
#     else:
#         arr = []
#         for i in range(n):
#             if i // len(stars(n//3)) == 1:
#                 arr.append(stars(n//3)[i%len(stars(n//3))] + ' '*(n//3) + stars(n//3)[i%len(stars(n//3))])
#             else:
#                 arr.append(stars(n//3)[i%len(stars(n//3))]*3)
#         return arr

def stars(star):
    arr = []
    for i in range(len(star)*3):
        if i // len(star) == 1:
            arr.append(star[i%len(star)] + ' '*(len(star)) + star[i%len(star)])
        else:
            arr.append(star[i%len(star)] * 3)
    return arr

n = int(input())
k = 0
while n // 3 != 1:
    n = n / 3
    k += 1

star = ['***','* *','***']

for i in range(k):
    star = stars(star)

print('\n'.join(star))

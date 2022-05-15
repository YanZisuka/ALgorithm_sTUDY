R = int(input())
rooms = list(map(int, input().split()))
N = int(input())

max = 0
sum1 = [0] * (R-(N*3)+1)
sum2 = [[0] * (R-(N*3)+1) for _ in range(R-(N*3)+1)]

for i in range(R-(N*3)+1):
    sum1[i] = sum(rooms[i:i+N])

print(sum1)

for i in range(R-(N*3)+1):
    for j in range(R-(N*3)+1):
        sum2[i][j] = (sum1[i] + sum(rooms[j+N:j+(N*2)]))

print(sum2)

for i in range(R-(N*3)+1):
    for j in range(R-(N*3)+1):
        for k in range(R-(N*3)+1):
            temp = sum2[i][j] + sum(rooms[k:k+N])
            if max < temp:
                max = temp

print(max)

# max = 0
# sum1 = [0] * R
# sum2 = [[0] * R for _ in range(R)]
#
# for i in range(R-(N*3)+1):
#     sum1[i] = sum(rooms[i:i+N])
#
# for i in range(R-(N*3)+1):
#     for j in range(i+N, R-(N*2)+1):
#         sum2[i][j] = (sum1[i] + sum(rooms[j:j+N]))
#
# for i in range(R-(N*3)+1):
#     for j in range(i+N, R-(N*2)+1):
#         for k in range(j+N, R-N+1):
#             temp = sum2[i][j] + sum(rooms[k:k+N])
#             if max < temp:
#                 max = temp
#
# print(max)

R = int(input())
rooms = list(map(int, input().split()))
N = int(input())

max = 0
for i in range(R-N+1):
    for j in range(i+1, R-N+1):
        for k in range(j+1, R-N+1):
            temp = sum(rooms[i:i+N] + rooms[j:j+N] + rooms[k:k+N])
            if max < temp:
                max = temp

print(max)

N = int(input())
sequence = list(map(int,input().split()))
mini_sequence = [[] for _ in range(N)]

for num in range(N):
    max_sequence = []
    for n in range(0,num):
        if sequence[num]>sequence[n]:
            if len(mini_sequence[n]) >= len(max_sequence):
                max_sequence = mini_sequence[n]
    mini_sequence[num]= max_sequence+[sequence[num]]

max_len = 0
for s in mini_sequence:
    if len(s)>max_len:
        max_len = len(s)
        answer = s
print(max_len)
print(*answer)


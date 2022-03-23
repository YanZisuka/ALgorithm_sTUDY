count = [1, 1]
for i in range(3, 91):
    count.append(count[i - 2] + count[i - 3])
N = int(input())
print(count[N - 1])

# N = 91 까지 리스트를 만들어 놓고 나중에 값을 입력받으면 통과
# 입력을 먼저 받고, 그 수까지만 리스트 만들면 런타임에러 (왜 시간초과가 아니고 런타임 에러 뜰까?)

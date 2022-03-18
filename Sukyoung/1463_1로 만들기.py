N = int(input())
count = [0 for _ in range(N+1)]

for i in range(2,N+1):
    count[i] = count[i-1]+1  # -1를 하는 경우 ( 앞 숫자와 같아지므로 앞 숫자 카운트 +1)

    if i%2 == 0:
        count[i] = min(count[i//2]+1,count[i]) # -1 하고 앞 숫자 카운트 그대로 가져오기 vs 나누기 2한 숫자 카운트 가져오기

    if i%3 == 0:
        count[i] = min(count[i//3]+1,count[i]) # -1 하고 앞 숫자 카운트 그대로 가져오기 vs 나누기 3한 숫자 카운트 가져오기

print(count[N])
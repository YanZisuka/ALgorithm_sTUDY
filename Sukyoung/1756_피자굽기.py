D, N = map(int,input().split())
oven = list(map(int,input().split()))
pizza = list(map(int,input().split()))
deep = D
for d in range(D-1): # 계단 모양으로 만들기 (앞이 작으면 그 뒤도 다 같은 값)
    if oven[d] < oven[d+1]:
        oven[d+1] = oven[d]

for p in pizza:
    if p > oven[0]:  # 첫 입구 크기부터 피자보다 작으면 결과 0
        deep = -1
        break
    if deep == 0:  # 끝까지 다 찼으면 결과 0
        deep = -1
        break
    for o in range(deep-1,-1,-1):  # 뒤에서 부터 탐색
        if oven[o] >= p:
            deep = o # 피자 넣은 곳 바로 위로 deep 갱신
            break

print(deep+1)



def electric_bus(k, n, m):
    stops = [0] * (n + 1)  # 정류장 세팅
    charge_cnt = 0  # 충전횟수 세팅
    chargers = list(map(int, input().split()))

    for i in chargers:  # 충전기 세팅
        stops[i] = 1

    # 주행
    distance = 0
    while distance + k < n:
        for move in range(k, -1, -1):
            if move == 0:
                return 0
            if stops[distance + move] == 1:
                charge_cnt += 1
                distance += move
                break
    return charge_cnt
    
    
t = int(input())
for tc in range(1, t+1):
    k, n, m = map(int, input().split())
    
    print(f'#{tc} {electric_bus(k, n, m)}')
    
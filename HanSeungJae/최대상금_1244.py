import sys
sys.stdin = open('input.txt')


t = int(input())
for tc in range(1, t+1):
    num, exchange = map(int, input().split())
    num = list(map(int, str(num)))
    target = sorted(num, reverse=True)
    
    for i in range(len(num)):  # 만들 수 있는 가장 큰 수인 target과 자리를 비교해 조건에 충족되면 교환
        if num[i] != target[i]:
            for j in range(i+1, len(num)):
                if num[j] != target[j] and num[j] == target[i]:
                    num[i], num[j] = num[j], num[i]
                    exchange -= 1
                    break
                    
        if exchange == 0:
            break
    
    if exchange:  # 가장 큰 수로 만들었음에도 교환 횟수가 남은 경우
        for i in range(len(num)):  # 숫자카드 중 같은 숫자가 2개 이상이면 그것들로 교환을 소모한다.
            for j in range(i+1, len(num)):
                if num[i] == num[j]:
                    exchange = 0
                    break
                    
            if exchange == 0:
                break
                
        while exchange:  # 같은 숫자가 없으면 일의 자리와 십의 자리만 계속 바꾼다.
            num[-1], num[-2] = num[-2], num[-1]
            exchange -= 1
            
    print(f'#{tc} {"".join(map(str, num))}')
    
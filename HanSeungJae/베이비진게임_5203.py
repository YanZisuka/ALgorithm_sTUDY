import sys
sys.stdin = open('input.txt')


def babyGin(arr):
    player1 = []
    player2 = []
    runCnt1, tripletCnt1 = 0, 0
    runCnt2, tripletCnt2 = 0, 0

    for i in range(12):
        if i % 2 == 0:
            player1.append(arr[i])
            player1.sort()
            if len(player1) > 2:
                for j in range(len(player1)-1):
                    if player1[j] == player1[j + 1]:
                        tripletCnt1 += 1
                    else:
                        tripletCnt1 = 0
                    if tripletCnt1 >= 2:
                        return 1
                    
                temp1 = list(set(player1))
                for j in range(len(temp1)-1):
                    if temp1[j] == temp1[j + 1] - 1:
                        runCnt1 += 1
                    else:
                        runCnt1 = 0
                    if runCnt1 >= 2:
                        return 1

        else:
            player2.append(arr[i])
            player2.sort()
            if len(player2) > 2:
                for j in range(len(player2)-1):
                    if player2[j] == player2[j + 1]:
                        tripletCnt2 += 1
                    else:
                        tripletCnt2 = 0
                    if tripletCnt2 >= 2:
                        return 2
                    
                temp2 = list(set(player2))
                for j in range(len(temp2)-1):
                    if temp2[j] == temp2[j + 1] - 1:
                        runCnt2 += 1
                    else:
                        runCnt2 = 0
                    if runCnt2 >= 2:
                        return 2
    return 0


t = int(input())
for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    
    print(f'#{tc} {babyGin(arr)}')
        
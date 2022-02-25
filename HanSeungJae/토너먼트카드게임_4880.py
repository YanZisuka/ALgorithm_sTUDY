import sys
sys.stdin = open('input.txt')


def rock_scissors_paper(player1, player2):
    if abs(cards[player1]-cards[player2]) == 0:
        return min(player1, player2)
    elif abs(cards[player1]-cards[player2]) == 1:
        return max(player1, player2, key=lambda x: cards[x])
    elif abs(cards[player1]-cards[player2]) == 2:
        return min(player1, player2, key=lambda x: cards[x])


def tournament(players):
    length = len(players)
    if length < 2:
        return players
    if length == 2:
        return [rock_scissors_paper(*players)]
    left = tournament(players[:length//2+length%2])
    right = tournament(players[length//2+length%2:])
    
    return tournament(left + right)
    


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    cards = list(map(int, input().split()))
    players = [n for n in range(len(cards))]
    
    print(f'#{tc} {tournament(players)[0]+1}')
    
N = int(input())
cards = list(map(int,input().split()))
M = int(input())
my_cards = list(map(int,input().split()))
cards.sort()

def find(card):
    start = 0
    end = len(cards) - 1
    while start <= end:
        middle = (start+end) // 2
        if card == cards[middle]:
            return 1
        elif card > cards[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return 0

for card in my_cards:
    print(find(card),end=' ')
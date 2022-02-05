from itertools import combinations
import sys
input = sys.stdin.readline

def black_jack(m, cards):
    card_sums = []

    for array in combinations(cards, 3):
        card_sums.append(sum(array))
    
    card_sums.sort()

    for i in range(len(card_sums)):
        if card_sums[i] > m:
            return card_sums[i-1]

    return card_sums[-1]


n, m = map(int, input().split())
cards = map(int, input().split())

print(black_jack(m, cards))
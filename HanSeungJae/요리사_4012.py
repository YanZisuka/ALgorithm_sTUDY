from itertools import combinations
import sys
sys.stdin = open('input.txt')


def BruteForce(ingredients):
    global answer
    for comb in combinations(ingredients, n // 2):
        ingredients = [i for i in range(n)]
        for ingredient in comb:
            ingredients.remove(ingredient)
        food1, food2 = 0, 0

        for synergy in combinations(comb, 2):
            i, j = synergy
            food1 += S[i][j]
            food1 += S[j][i]
        for synergy in combinations(ingredients, 2):
            i, j = synergy
            food2 += S[i][j]
            food2 += S[j][i]

        answer = min(answer, abs(food1 - food2))


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    S = [list(map(int, input().split())) for _ in range(n)]
    ingredients = [i for i in range(n)]
    answer = float('INF')
    
    BruteForce(ingredients)
            
    print(f'#{tc} {answer}')
import sys
read = sys.stdin.readline

word1 = read().strip()
word2 = read().strip()

cache = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

for i in range(1, len(word1) + 1):
    for j in range(1, len(word2) + 1):
        if word1[i-1] == word2[j - 1]:
            cache[i][j] = cache[i - 1][j - 1] + 1
        else:
            cache[i][j] = max(cache[i][j - 1], cache[i - 1][j])

print(cache[len(word1)][len(word2)])
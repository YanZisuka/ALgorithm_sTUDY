import sys
input = sys.stdin.readline


def isGroupWord(word):
    stack = []
    
    for i in range(len(word)):
        if not stack:
            stack.append(word[i])
        else:
            if word[i] in stack and word[i] != stack[-1]:
                return False
            elif word[i] not in stack:
                stack.append(word[i])
    return True


n = int(input())
answer = 0

for _ in range(n):
    st = input().strip()
    if isGroupWord(st):
        answer += 1

print(answer)
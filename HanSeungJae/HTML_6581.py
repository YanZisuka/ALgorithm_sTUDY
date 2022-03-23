import sys
sys.stdin = open('input.txt')

fullSt = []
lineLen = 0
while True:
    try:
        for word in input().split():
            if word == '<br>':
                lineLen = 0
                fullSt.append('\n')
            elif word == '<hr>':
                if lineLen:
                    fullSt.append('\n')
                    fullSt.append('-' * 80)
                    fullSt.append('\n')
                else:
                    fullSt.append('-' * 80)
                    fullSt.append('\n')
                lineLen = 0
            else:
                wordLen = len(word)
                if lineLen + wordLen > 80:
                    lineLen = wordLen
                    fullSt.append('\n')
                    fullSt.append(word)
                else:
                    lineLen += wordLen
                    fullSt.append(word)
                if lineLen + 1 > 80:
                    lineLen = 0
                    fullSt.append('\n')
                else:
                    lineLen += 1
                    fullSt.append(' ')
    except:
        for i in range(len(fullSt)):
            if fullSt[i] == '\n' and fullSt[i-1] == ' ':
                fullSt[i-1] = ''
        fullSt[-1] = ''
        print(''.join(fullSt))
        break

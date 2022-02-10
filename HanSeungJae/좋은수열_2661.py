import sys
input = sys.stdin.readline

def good_array(idx):
    for i in range(1, (idx//2) + 1):
        if s[-i:] == s[-2*i:-i]:
            return -1

    if idx == n:
        for i in range(n):
            print(s[i], end = '')
        return 0

    for i in range(1, 4):
        s.append(i)
        if good_array(idx + 1) == 0:
            return 0
        s.pop()


n = int(input())
s = []
good_array(0)
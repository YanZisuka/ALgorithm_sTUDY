import sys
input = sys.stdin.readline

N = int(input())

def hansu(N):
    cnt = 0
    for i in range(1, N+1):
        d = set()
        if i < 10:
            cnt += 1
        else:
            for j in range(1, len(str(i))):
                d.add(int(str(i)[j]) - int(str(i)[j-1]))
            if len(d) == 1:
                cnt += 1
    return cnt
            
print(hansu(N))
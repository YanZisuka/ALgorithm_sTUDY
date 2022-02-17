# 좋은 수열의 판별
def check(num):
    length = len(num)
    for idx in range(1, length//2 + 1): #길이의 반(몫)만큼
        if num[-idx:] == num[-(idx*2):-idx]: #반복시
            return False
    else:
        return True

# 수열 생성 재귀함수
def recursive(num):
    global N, res
    if len(num) == N:
        print(num)
        exit()
    for i in '123':
        if check(num + str(i)):
            recursive(num + str(i))
    return

N = int(input())
recursive('1')
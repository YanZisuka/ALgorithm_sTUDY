hh, mm = map(int, input().split())
time = int(input())

temp = hh * 60 + mm + time
hh = temp // 60
mm = temp % 60

if hh >= 24:
    hh -= 24

print(f'{hh} {mm}')
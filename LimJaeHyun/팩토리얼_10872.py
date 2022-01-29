def Kwang(num):
    if num > 1:
        return num * Kwang(num - 1)
    else:
        return 1
N = int(input())

print(Kwang(N))
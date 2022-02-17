def make_max_min(cnt, result, plus, minus, multi, div):
    global result_max
    global result_min
    if cnt == N:
        result_max = max(result, result_max)
        result_min = min(result, result_min)
        return True
    if plus:
        make_max_min(cnt+1, result+numbers[cnt], plus-1, minus, multi,div)
    if minus:
        make_max_min(cnt+1, result-numbers[cnt], plus, minus-1, multi, div)
    if multi:
        make_max_min(cnt+1, result*numbers[cnt], plus, minus, multi-1, div)
    if div:
        if result < 0:
            make_max_min(cnt+1, -(-result//numbers[cnt]), plus, minus, multi, div-1)
        else:
            make_max_min(cnt+1, result//numbers[cnt], plus, minus, multi, div-1)

N = int(input())
numbers = list(map(int,input().split()))
operators = list(map(int,input().split()))
result_max = -float('inf')
result_min = float('inf')

make_max_min(1, numbers[0], operators[0], operators[1], operators[2], operators[3])
print(result_max)
print(result_min)
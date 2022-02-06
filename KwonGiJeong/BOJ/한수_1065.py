def numbers_maker(number):
    numbers = []
    while number > 0:
        numbers.append(number%10)
        number = number // 10
    return numbers
        
def is_han_number(numbers):
    if len(numbers) <= 2:
        return True
    else:
        for i in range(len(numbers)-2):
            if ((numbers[i+1] - numbers[i]) != (numbers[i+2] - numbers[i+1])):
                return False
        return True
            
def cnt_han_number(n):
    cnt = 0
    for j in range(1, n+1):
        if is_han_number(numbers_maker(j)):
            cnt += 1
    return cnt

N = input()
sn = int(N)
result = cnt_han_number(sn)
print(result)
def fibonacci(number):
    if (number == 0) or (number == 1):
        return number
    else:
        return (fibonacci(number-1) + fibonacci(number-2))
            
N = input()
sn = int(N)
result = fibonacci(sn)
print(result)
def factorial(number):
    if number > 1:
        return (number * factorial(number-1))
    else:
        return 1

N = input()
sn = int(N)
result = factorial(sn)
print(result)
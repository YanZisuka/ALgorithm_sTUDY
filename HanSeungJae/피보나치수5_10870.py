def my_fib(n):
    if n < 2:
        return n
    else:
        return my_fib(n-1) + my_fib(n-2)

n = int(input())
print(my_fib(n))
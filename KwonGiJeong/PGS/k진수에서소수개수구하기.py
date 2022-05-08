import math

def get_k_number(n, k):
    new_n = ''
    
    while n > 0:
        new_n = str(n % k) + new_n
        n = n // k
        
    return new_n


def is_prime_number(n):
    answer = True
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            answer = False
            break
    
    return answer



def solution(n, k):
    
    answer = 0
    numbers = get_k_number(n, k).split('0')
    
    for number in numbers:
        if not (number == '1' or number == ''):
            if is_prime_number(int(number)):
                answer += 1
    
    return answer
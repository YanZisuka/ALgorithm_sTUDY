def solution(n, k):

    def is_prime(x):
        for i in range(2,int(x**0.5)+1):
                if x % i == 0:
                    return False
        return True

    result=[]
    quotient = n
    answer = 0

    while quotient != 0:
        remainder = quotient % k
        result.append(str(remainder))
        quotient = quotient // k

    result.reverse()
    result = (''.join(result)).split('0')
    print(result)
    for num in result:
        if num and num != '1':
            if is_prime(int(num)):
                answer += 1

    return answer
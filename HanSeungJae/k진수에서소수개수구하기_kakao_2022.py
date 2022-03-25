def solution(n, k):
    n = int(n)
    k = int(k)
    
    def getK(n):
        prime_num = ''
        while n // k != 0:
            prime_num = str(n % k) + prime_num
            n = n // k
        prime_num = str(n % k) + prime_num
        
        return int(prime_num)
    
    def check(num):
        if num:
            num = int(num)
            max_val = int(num**0.5)
            
            if num == 1:
                return False

            for i in range(2, max_val+1):
                if num % i == 0:
                    return False
                
            return True
    
    ans = 0
    
    n = str(getK(n))
    idx = 0
    
    for i in range(len(n)):
        if n[i] != '0' and i == len(n) - 1:
            num = n[idx:]
            if check(num):
                ans += 1
                
        if n[i] == '0':
            num = n[idx:i]
            if check(num):
                ans += 1
            idx = i+1
    
    return ans
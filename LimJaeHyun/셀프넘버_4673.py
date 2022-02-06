def self_num(n):
    self_list = []
    not_self_list = []

    for num in range (1, n + 1):
        jjogae = []
        jjogae.append(num)
        for i in str(num):
            jjogae.append(int(i))
        not_self_list.append(sum(jjogae))

    for number in range(1, n + 1):
        if number not in not_self_list:
            self_list.append(number)
    
    for number in self_list:
        print(number)

self_num(10000)
    
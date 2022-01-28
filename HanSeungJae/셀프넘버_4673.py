def self_num(n):
    n_list = list(range(1, n+1))
    d_n_list = []
    sel_list = []
    
    for i in range(1, n+1):
        d_n = i
        while i // 10 != 0:
            d_n += i % 10
            i = i // 10
        d_n += i

        d_n_list.append(d_n)
    
    for num in n_list:
        if num not in d_n_list:
            sel_list.append(num)

    for n in sel_list:
        print(n)

self_num(10000)
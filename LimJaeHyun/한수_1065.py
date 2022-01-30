def Hansu_panbyeol(N):
    Hansu_string = str(N)
    N_listed = []
    diff_list = []
    for num in Hansu_string:
        N_listed.append(int(num))
    for idx in range(1, len(N_listed)):
        diff_list.append(N_listed[idx] - N_listed[idx - 1])
    if len(set(diff_list)) == 1:
        return True
    elif N < 10 :
        return True

def Hansu_listing(N):
    Hansu_list = []
    for num in range(1, N + 1):
        if Hansu_panbyeol(num) == True:
            Hansu_list.append(num)
    return len(Hansu_list)


print(Hansu_listing(int(input())))

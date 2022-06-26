def solution(n, arr1, arr2):
    def conv(num):
        st = ''
        while num != 0:
            st = str(num % 2) + st
            num //= 2

        while len(st) < n:
            st = '0' + st

        return st

    conv_arr1 = list(map(conv, arr1))
    conv_arr2 = list(map(conv, arr2))

    board = ['' for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if conv_arr1[i][j] == '0' and conv_arr2[i][j] == '0':
                board[i] += ' '
            else:
                board[i] += '#'

    return board





print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))  # ["#####","# # #", "### #", "# ##", "#####"]
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))  # ["######", "### #", "## ##", " #### ", " #####", "### # "]
def solution(n, arr1, arr2):
    binary_arr1 = []
    binary_arr2 = []
    answer = []
    for decimal in arr1:
        if decimal == 0:
            binary = '0'
        else:
            binary = bin(decimal).lstrip('0b')
        binary_arr1.append(int(binary))
    for decimal in arr2:
        if decimal == 0:
            binary = '0'
        else:
            binary = bin(decimal).lstrip('0b')
        binary_arr2.append(int(binary))
    for i in range(n):
        answer.append(list(str(binary_arr1[i] + binary_arr2[i]).zfill(n)))
    print(answer)
    for i in range(n):
        for j in range(n):
            if answer[i][j] == '0':
                answer[i][j] = ' '
            else:
                answer[i][j] = '#'
        answer[i] = ''.join(answer[i])
    print(answer)
    return answer


solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
solution(5, [0,0,0,0,0], [0,0,0,0,0])

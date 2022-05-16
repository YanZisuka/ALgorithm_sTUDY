def solution(dartResult):
    SDT = ['S', 'D', 'T']
    num_list = []
    for i in dartResult:
        if i.isdecimal():
            num_list.append(int(i))

            if len(num_list) > 1 and num_list[-1] == 0 and num_list[-2] == 1:
                num_list[-2] = 10
                num_list.pop()

        elif i.isalpha():
            num_list[-1] **= (SDT.index(i) + 1)

        else:
            if i == '*':
                num_list[-1] *= 2

                if len(num_list) > 1:
                    num_list[-2] *= 2
            else:
                num_list[-1] *= (-1)

    answer = sum(num_list)
    return answer
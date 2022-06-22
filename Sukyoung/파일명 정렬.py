def solution(files):
    answer = []
    file_list = []
    for file in files:
        head = ''
        number = ''
        for f in range(len(file)):
            if file[f].isdecimal():
                idx = f
                break
            if file[f].isalpha():
                a = file[f].lower()
                head += a
            else:
                head += file[f]

        for l in range(f, len(file)):
            if not file[l].isdecimal():
                break
            number += file[l]

        file_list.append([file, head, number])

    file_list.sort(key=lambda x: (x[1], int(x[2])))

    answer = [i[0] for i in file_list]

    return answer
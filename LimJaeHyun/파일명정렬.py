def solution(files):
    answer = ['' for _ in range(len(files))]
    temp = []
    for index, file in enumerate(files):
        file = file.upper()
        file = list(file)
        head = ''
        number = ''
        tail = ''
        for char in file:
            if (char.isalpha() or char == '.' or char == '-' or char == ' ') and number == '':
                head += char
            elif char.isdigit() and tail == '':
                number += char
            else:
                tail += char
        splitted = [head, int(number), index]
        temp.append(splitted)
    temp.sort()
    for index, name in enumerate(temp):
        answer[index] = files[name[2]]
    print(answer)
    return answer


solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])

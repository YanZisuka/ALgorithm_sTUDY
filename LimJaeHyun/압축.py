def solution(msg):
    answer = []
    dictionary = ['ㅁ', 'A', 'B', 'C', 'D', 'E', 'F',
                  'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S',
                  'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    message = list(msg + '0')
    temp = ''
    for char in message:
        if temp + char not in dictionary:
            dictionary.append(temp + char)
            answer.append(dictionary.index(temp))
            temp = char
        else:
            temp += char
    print(answer)
    print(dictionary)
    return answer


solution('KAKAO')
solution('TOBEORNOTTOBEORTOBEORNOT')
solution('ABABABABABABABAB')

def solution(s):

    englsih = ['zero', 'one', 'two', 'three', 'four',
               'five', 'six', 'seven', 'eight', 'nine']

    if s.isdigit():
        return int(s)

    answer = ''
    temp = ''
    for word in s:
        if word.isdigit():
            answer += word
        else:
            temp += word
            if temp in englsih:
                answer += str(englsih.index(temp))
                temp = ''

    return int(answer)

def solution(s):
    answer = ''
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    string = list(s)
    print(string)
    temp = ''
    for character in string:
        if character.isdigit():
            answer += character
        elif character.isalpha():
            temp += character
            if temp in numbers:
                answer += str(numbers.index(temp))
                temp = ''
    answer = int(answer)
    print(answer)
    return answer


# solution('one4seveneight')
# solution('23four5six7')
# solution('2three45sixseven')
# solution('123')

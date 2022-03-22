def solution(s):
    words = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    
    for k, v in words.items():
        s = s.replace(k, v)
                
    answer = int(s)
    return answer
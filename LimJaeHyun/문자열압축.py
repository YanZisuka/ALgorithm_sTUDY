def solution(s):
    answer = float('inf')
    for i in range(1, (len(s)//2) + 1):
        previous = ''
        cnt = 0
        compressed = ''
        for j in range(0, len(s), i):
            if not previous:
                previous = s[j:j+i]
                cnt += 1
            else:
                current = s[j:j+i]
                if current == previous:
                    cnt += 1
                else:
                    compressed += f'{cnt}{previous}' if cnt != 1 else f'{previous}'
                    cnt = 1
                    previous = current
        compressed += f'{cnt}{previous}' if cnt != 1 else f'{previous}'
        if len(compressed) < answer:
            answer = len(compressed)
    if len(s) == 1: answer = 1
    return answer


solution("aabbaccc") # 7
solution("ababcdcdababcdcd") # 9
solution("abcabcdede") # 8
solution("abcabcabcabcdededededede") # 14
solution("xababcdcdababcdcd")  # 17

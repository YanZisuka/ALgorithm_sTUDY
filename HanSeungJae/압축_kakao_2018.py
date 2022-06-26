from string import ascii_uppercase

def solution(msg):
    table = {a:i+1 for i, a in enumerate(ascii_uppercase)}
    answer = []
    i = 0

    while i < len(msg):
        key = msg[i]
        k = 1
        for _ in range(len(msg) - (i + 1)):
            key = msg[i : i + k + 1]
            if not table.get(key):
                key = msg[i : i + k]
                break
            k += 1
        answer.append(table.get(key))
        table[msg[i : i + k + 1]] = len(table) + 1
        i += k

    return answer





print(solution('KAKAO'))  # [11, 1, 27, 15]
print(solution('TOBEORNOTTOBEORTOBEORNOT'))  # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print(solution('ABABABABABABABAB'))  # [1, 2, 27, 29, 28, 31, 30]
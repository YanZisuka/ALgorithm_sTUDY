def solution(s):
    answer = 0

    if len(s) == 1:
        answer = 1

    else:
        result = []

        for unit in range(1, len(s) + 1):
            zip = ''
            tmp = s[:unit]
            cnt = 1

            for i in range(unit, len(s) + unit, unit):

                if tmp == s[i:unit + i]:
                    cnt += 1

                else:
                    if cnt != 1:
                        zip = zip + str(cnt) + tmp
                    else:
                        zip = zip + tmp

                    tmp = s[i:i + unit]
                    cnt = 1

            result.append(len(zip))

        answer = min(result)

    return answer

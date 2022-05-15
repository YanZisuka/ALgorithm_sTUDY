def solution(dartResult):
    stack = []

    for i in range(len(dartResult)):
        char = dartResult[i]
        if char == 'S': pass
        elif char == 'D': stack[-1] **= 2
        elif char == 'T': stack[-1] **= 3
        elif char == '*':
            if len(stack) > 1:
                stack[-2], stack[-1] = stack[-2] * 2, stack[-1] * 2
            else:
                stack[-1] *= 2
        elif char == '#': stack[-1] *= -1
        elif char == '1':
            if dartResult[i+1] == '0':
                pass
            else:
                stack.append(int(char))
        elif char == '0':
            if dartResult[i-1] == '1':
                stack.append(10)
            else:
                stack.append(int(char))
        else: stack.append(int(char))

    answer = sum(stack)

    return answer





print(solution('1S2D*3T'))  # 37
print(solution('1D2S#10S'))  # 9
print(solution('1D2S0T'))  # 3
print(solution('1S*2T*3S'))  # 23
print(solution('1D#2S*3S'))  # 5
print(solution('1T2D3D#'))  # -4
print(solution('1D2S3T*'))  # 59
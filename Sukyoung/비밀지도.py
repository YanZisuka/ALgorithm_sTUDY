def solution(n, arr1, arr2):
    def make_map(arr):
        for a in range(n):
            binary = [0] * n
            q = arr[a]
            idx = -1

            if q == 0:
                arr[a] = binary

            else:
                while q != 1:
                    b = q % 2
                    q = q // 2
                    binary[idx] = b
                    idx -= 1

                binary[idx] = 1
                arr[a] = binary
        return arr

    arr1 = make_map(arr1)
    arr2 = make_map(arr2)

    answer = []
    for i in range(n):
        line = ''
        for j in range(n):
            if arr1[i][j] == 0 and arr2[i][j] == 0:
                line += ' '
            else:
                line += '#'
        answer.append(line)

    return answer
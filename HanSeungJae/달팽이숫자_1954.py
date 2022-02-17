import sys
sys.stdin = open('input.txt')

def slug(n):
    matrix = [[0] * n for _ in range(n)]
    matrix[0][0] = 1
    i = j = 0
    for num in range(2, n ** 2 + 1):  # 2부터 n**2까지 순회
        for direction in range(4):  # 0: 오른쪽 1: 아래 2: 왼쪽 3:위
            if direction == 0:
                j += 1
                if j >= n or matrix[i][j] != 0 or matrix[i+1][j-1] != 0 and matrix[i-1][j-1] == 0:  # 오른쪽으로 가지 말아야 할 경우
                    j -= 1
                    continue  # 아래쪽으로 방향 설정
                matrix[i][j] = num  # 오른쪽 조건이 맞다면 number를 그 자리에 할당
                break  # number를 할당했으므로 number를 1 늘린다.
            elif direction == 1:
                i += 1
                if i >= n or matrix[i][j] != 0:  # 아래로 가지 말아야 할 경우
                    i -= 1
                    continue  # 왼쪽으로 방향 설정
                matrix[i][j] = num
                break
            elif direction == 2:
                j -= 1
                if j >= n or matrix[i][j] != 0:
                    j += 1
                    continue
                matrix[i][j] = num
                break
            elif direction == 3:
                i -= 1
                if i >= n or matrix[i][j] != 0:
                    i += 1
                    continue
                matrix[i][j] = num
                break
    for i in range(n):
        matrix[i] = ' '.join(map(str, matrix[i]))
    return '\n'.join(map(str, matrix))


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    
    print(f'#{tc}\n{slug(n)}')
    
                
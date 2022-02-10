def change_boxes(N, Q):
    boxes = [0] * N  # n개의 길이를 갖는 박스 생성

    for i in range(1, Q + 1):  # Q회 동안 i번째 작업에 대해 L번부터 R번까지 상자값 i로 변경
        L, R = map(int, input().split())
        boxes[L-1:R] = [i] * (R-L+1)
        
    return ' '.join(map(str, boxes))


t = int(input())
for tc in range(1, t+1):
    n, q = map(int, input().split())

    print(f'#{tc} {change_boxes(n, q)}')
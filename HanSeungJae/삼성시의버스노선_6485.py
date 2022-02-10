def bus(n):
    c = [0] * 5001  # 0~5000의 인덱스를 갖는 정류장 생성
    o = []  # P에서 선언된 정류장만 출력할 리스트 생성
    for i in range(1, n + 1):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            c[i] += 1  # a번째 정류장부터 b번째 정류장까지 방문하는 버스 한 개 추가

    p = int(input())
    for _ in range(p):
        j = int(input())
        o.append(c[j])  # 출력할 아웃풋에 P에서 선언된 정류장만 차례대로 추가
        
    return ' '.join(map(str, o))


t = int(input())
for tc in range(1, t+1):
    n = int(input())

    print(f'#{tc} {bus(n)}')
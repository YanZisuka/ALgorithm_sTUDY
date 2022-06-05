def solution(n, build_frame):
    frame = [[0] * (n) for _ in range(n)]
    print(frame)
    answer = []
    for bf in build_frame:
        if bf[3] == 1:  # 설치
            if bf[2] == 0:  # 기둥
                if bf[1] + 1 < n:
                    if bf[1] == 0 or frame[bf[0]][bf[1]] != 0:
                        answer.append([bf[0], bf[1], bf[2]])
                        frame[bf[0]][bf[1] + 1] = 1

            else:  # 보
                if bf[0] + 1 < n:
                    if frame[bf[0]][bf[1]] == 1 or frame[bf[0] + 1][bf[1]] == 1 or (
                            frame[bf[0]][bf[1]] == 2 and frame[bf[0] + 1][bf[1]] == 2):
                        if frame[bf[0]][bf[1]] == 0:
                            frame[bf[0]][bf[1]] = 2
                        if frame[bf[0] + 1][bf[1]] == 0:
                            frame[bf[0] + 1][bf[1]] = 2
                        answer.append([bf[0], bf[1], bf[2]])



        else:
            answer.remove([bf[0], bf[1], bf[2]])

    answer.sort(key=lambda x: (x[0], x[1]))
    return answer

solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
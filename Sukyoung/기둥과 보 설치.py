def solution(n, build_frame):
    frame = [[0] * (n + 1) for _ in range(n + 1)]
    answer = []
    for bf in build_frame:
        if bf[3] == 1:  # 설치
            if bf[2] == 0:  # 기둥
                if bf[1] + 1 < n + 1:
                    if bf[1] == 0 or frame[bf[1]][bf[0]] != 0:
                        answer.append([bf[0], bf[1], bf[2]])
                        frame[bf[1] + 1][bf[0]] += 2

            else:  # 보
                if bf[0] + 1 < n + 1:
                    if frame[bf[1]][bf[0]] > 1 or frame[bf[1]][bf[0] + 1] > 1 or (
                            frame[bf[1]][bf[0]] == 1 and frame[bf[1]][bf[0] + 1] == 1):
                        frame[bf[1]][bf[0]] += 1
                        frame[bf[1]][bf[0] + 1] += 1
                        answer.append([bf[0], bf[1], bf[2]])



        else:
            if bf[2] == 0 and bf[1] + 1 < n + 1 and 0 <= bf[0] - 1 and bf[0] + 1 < n + 1:  # 기둥
                frame[bf[1] + 1][bf[0]] -= 2
                if (frame[bf[1] + 1][bf[0] - 1] == 1 and frame[bf[1] + 1][bf[0]] == 1) or (
                        frame[bf[1] + 1][bf[0] + 1] == 1 and frame[bf[1] + 1][bf[0]] == 1) or (
                        frame[bf[1] + 1][bf[0]] >= 2 and frame[bf[1] + 1][bf[0]] == 0):

                    frame[bf[1] + 1][bf[0]] += 2
                else:
                    answer.remove([bf[0], bf[1], bf[2]])
            else:  # 보
                frame[bf[1]][bf[0]] -= 1
                frame[bf[1]][bf[0] + 1] -= 1
                if (frame[bf[1] + 1][bf[0]] >= 2 and frame[bf[1]][bf[0]] == 0) or (
                        frame[bf[1] + 1][bf[0] + 1] >= 2 and frame[bf[1]][bf[0] + 1] == 0) or (
                        frame[bf[1]][bf[0]] == 1 and frame[bf[1]][bf[0] + 1] < 3):
                    frame[bf[1]][bf[0]] += 1
                    frame[bf[1]][bf[0] + 1] += 1
                else:
                    answer.remove([bf[0], bf[1], bf[2]])

    answer.sort(key=lambda x: (x[0], x[1]))
    return answer
def solution(lines):
    start_finish = []
    for l in lines:
        date, s, t = l.split()
        h, m, sec = s.split(':')
        sec = int(float(sec) * 1000) + (int(h) * 3600 + int(m) * 60) * 1000
        start_finish.append([sec - (int(float(t[:-1]) * 1000)) + 1, sec])

    cnt_list = []
    if len(start_finish) == 1:
        answer = 1
    else:
        for sf in range(len(start_finish) - 1):
            cnt = 0

            for next in start_finish[sf + 1:]:

                if (next[0] - start_finish[sf][1]) < 1000:
                    cnt += 1
            cnt_list.append(cnt)

        answer = max(cnt_list) + 1

    return answer
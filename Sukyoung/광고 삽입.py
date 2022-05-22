def solution(play_time, adv_time, logs):
    play = int(play_time[0:2]) * 3600 + int(play_time[3:5]) * 60 + int(play_time[6:])
    adv = int(adv_time[0:2]) * 3600 + int(adv_time[3:5]) * 60 + int(adv_time[6:])
    time = [0] * (play + 2)

    for log in logs:
        start, end = log.split('-')
        sh, sm, ss = start.split(':')
        eh, em, es = end.split(':')

        start_sec = int(sh) * 3600 + int(sm) * 60 + int(ss)
        end_sec = int(eh) * 3600 + int(em) * 60 + int(es)
        time[start_sec + 1] += 1
        time[end_sec + 1] -= 1

    for t in range(len(time) - 1):
        time[t + 1] += time[t]
    for t in range(len(time) - 1):
        time[t + 1] += time[t]

    max_time = 0

    for t in range(adv, play + 1):
        if t == adv:
            max_time = time[t]
            ad = t - adv
        else:
            if time[t] - time[t - adv] > max_time:
                max_time = time[t] - time[t - adv]
                ad = t - adv

    h = str(ad // 3600)
    m = str((ad % 3600) // 60)
    s = str((ad % 3600) % 60)

    answer = f'{h.zfill(2)}:{m.zfill(2)}:{s.zfill(2)}'
    return answer
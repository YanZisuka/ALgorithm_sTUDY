def solution(n, t, m, timetable):
    for i in range(len(timetable)):
        hour, minute = timetable[i].split(':')
        timetable[i] = int(hour) * 60 + int(minute)
    timetable.sort()

    now = 540
    for i in range(n):
        bus = []
        cnt = 0
        for c in range(len(timetable)):
            if now >= timetable[c] and cnt < m:
                bus.append(timetable[c])
                timetable[c] = 1000000
                cnt += 1

        if i == n - 1:
            if cnt == m:
                answer = bus[-1] - 1
            else:
                answer = now
        now += t

    answer = f'{str(answer // 60).zfill(2)}:{str(answer % 60).zfill(2)}'
    return answer
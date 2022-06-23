def solution(m, musicinfos):
    def make_melody(music):
        melody = []
        for m in range(len(music)):
            if music[m] == '#':
                melody[-1] = melody[-1] + '#'
            else:
                melody.append(music[m])
        return melody

    answer = []
    radio_music = []
    m = make_melody(m)

    for musicinfo in musicinfos:
        total_music = []
        music = musicinfo.split(',')
        end = music[1].split(':')
        start = music[0].split(':')
        time = (int(end[0]) * 60 + int(end[1])) - (int(start[0]) * 60 + int(start[1]))
        melody = make_melody(music[3])

        for i in range(time):
            total_music.append(melody[i % len(melody)])
            if total_music[-len(m):] == m:
                answer.append([time, music[2]])

    if answer:
        answer.sort(key=lambda x: -x[0])
        return answer[0][1]

    else:
        return "(None)"
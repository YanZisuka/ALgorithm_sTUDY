def get_max_emotion(happy, angry, sad, joy, words):

    words_list = words.split()
    emotion_cnt = [0] * 4
    emotions = ['happy', 'angry', 'sad', 'joy']

    for word in words_list:
        if happy.count(word):
            emotion_cnt[0] += 1
        elif angry.count(word):
            emotion_cnt[1] += 1
        elif sad.count(word):
            emotion_cnt[2] += 1
        elif joy.count(word):
            emotion_cnt[3] += 1

    max_index = 0
    max_value = -1

    for i in range(4):
        if emotion_cnt[i] >= max_value:
            max_index = i
            max_value = emotion_cnt[i]

    return emotions[max_index]


def solution(happy, angry, sad, joy, song):

    answer = []

    for words in song:
        answer.append(get_max_emotion(happy, angry, sad, joy, words))

    return answer
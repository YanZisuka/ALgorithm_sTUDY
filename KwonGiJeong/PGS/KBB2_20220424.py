result = []

def dfs(i, words, words_index, salary_index, false_cnt):

    global result

    word_list = list(words)
    salary_words = ['s', 'a', 'l', 'a', 'r', 'y']

    if word_list[words_index] == salary_words[salary_index]:
        if salary_index == 5:
            result[i] += 1
        elif salary_index == 4 and false_cnt < 2:
            result[i] += 1
        elif words_index + 1 < len(words):
            dfs(i, words, words_index + 1, salary_index + 1, false_cnt)

    elif word_list[words_index] != salary_words[salary_index]:
        false_cnt += 1

        if false_cnt > 1 and words_index + 1 < len(words):
            false_cnt = 0
            dfs(i, words, words_index, 0, false_cnt)

        elif words_index + 1 < len(words):
            dfs(i, words, words_index + 1, salary_index + 1, false_cnt)


def solution(deposit):

    global result
    answer = 0
    result = [0] * len(deposit)

    for i in range(len(deposit)):
        row_list = deposit[i].split()
        dfs(i, row_list[0], 0, 0, 0)
        print(result)
        if result[i] > 0:
            answer += int(row_list[1])

    return answer
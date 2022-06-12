def solution(word, pages):
    answer = 0
    page_list = []
    for page in pages:
        page_dict = {}
        parsing = page.split('\n')

        page_dict['name'] = parsing[3].split('=')[-1]
        page_dict['link'] = []
        page_dict['content'] = []
        page_dict['basic'] = 0

        body = parsing[6:-2]
        for i in range(len(body)):
            if i % 2:
                page_dict['link'].append(body[i])
            else:
                page_dict['content'].append(body[i])
        for words in page_dict['content']:
            for w in range(len(words)):
                words = list(words)
                if not words[w].isalpha():
                    words[w] = ' '
            words = (''.join(words)).split()

            for w in words:
                if w.lower() == word.lower():
                    page_dict['basic'] += 1
        page_dict['e_link'] = len(page_dict['link'])

        page_list.append(page_dict)
    print(page_list)
    return answer
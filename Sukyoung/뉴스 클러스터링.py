def solution(str1, str2):
    def make_list(x):
        result = []
        for i in range(len(x) - 1):
            word = x[i].lower() + x[i + 1].lower()
            if word.isalpha():
                result.append(word)
        return result

    list1 = make_list(str1)
    list2 = make_list(str2)

    its = []
    c_list1 = []
    for w in list1:
        if w in list2:
            its.append(w)
            list2.remove(w)
        else:
            c_list1.append(w)

    union = its + c_list1 + list2
    if not union:
        return 65536
    else:
        answer = (len(its) / len(union)) * 65536

    return int(answer)
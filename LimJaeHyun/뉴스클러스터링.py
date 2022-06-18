import copy


def solution(str1, str2):
    set1 = []
    set2 = []

    for i in range(0, len(str1)):  # 유효한 것들 리스트로 만들기 (집합이지만 집합 연산을 사용할 수 없다.)
        try:
            if str(str1[i] + str1[i+1]).isalpha():

                set1.append(str(str1[i] + str1[i+1]).upper())
        except IndexError:
            continue
    for i in range(0, len(str2)):
        try:
            if str(str2[i] + str2[i+1]).isalpha():
                set2.append(str(str2[i] + str2[i+1]).upper())
        except IndexError:
            continue

    set1_temp = set1.copy()
    set1_union = set1.copy()  # 합집합
    set1_intersection = []
    for element in set2:
        if element not in set1_temp:
            set1_union.append(element)
        else:
            set1_temp.remove(element)

    set1_temp = set1.copy()
    for element in set2: # 교집합
        if element in set1_temp:
            set1_temp.remove(element)
            set1_intersection.append(element)

    jaccard_similarity = len(set1_intersection) / len(set1_union) if len(set1_intersection) !=0 or len(set1_union) != 0 else 1
    answer = int(jaccard_similarity * 65536)
    print(answer)
    return answer


solution('FRANCE', 'french')
solution('handshake', 'shake hands')
solution('aa1+aa2', 'AAAA12')
solution('E=M*C^2', 'e=m*c^2')

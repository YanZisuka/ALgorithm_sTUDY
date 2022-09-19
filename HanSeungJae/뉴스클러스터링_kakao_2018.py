def solution(str1, str2):
    def compare(table1, table2):
        inter_charset = set()
        union_charset = set(list(table1.keys()) + list(table2.keys()))
        for k in table1.keys():
            if table2.get(k):
                inter_charset.add(k)
        intersection, union = 0, 0
        for char in inter_charset:
            intersection += min(int(table1.get(char) if table1.get(char) else 0), int(table2.get(char) if table2.get(char) else 0))
        for char in union_charset:
            union += max(int(table1.get(char) if table1.get(char) else 0), int(table2.get(char) if table2.get(char) else 0))

        if intersection == 0 and union == 0: return 1
        return intersection / union


    table1 = {}
    table2 = {}

    for i, char in enumerate(str1):
        st = str1[i:i+2].upper()
        if not st.isalpha() or len(st) < 2: continue
        if table1.get(st): table1[st] += 1
        else: table1[st] = 1

    for i, char in enumerate(str2):
        st = str2[i:i+2].upper()
        if not st.isalpha() or len(st) < 2: continue
        if table2.get(st): table2[st] += 1
        else: table2[st] = 1

    answer = compare(table1, table2)

    return int(answer * 65536)





print(solution('FRANCE', 'french'))  # 16384
print(solution('handshake', 'shake hands'))  # 65536
print(solution('aa1+aa2', 'AAAA12'))  # 43690
print(solution('E=M*C^2', 'e=m*c^2'))  # 65536
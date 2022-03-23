import re

t = int(input())
for tc in range(1, t+1):
    compares = []
    for _ in range(2):
        st = input().lower()
        st = re.sub(' +', ' ', st)
        st = st[1:] if st and st[0] == ' ' else st
        st = st[:-1] if st and st[-1] == ' ' else st
        st = list(st)
        for i in range(len(st)):
            if st[i] in ['(', ')', '[', ']', '{', '}', '.', ',', ';', ':']:
                if i != 0 and st[i-1] == ' ':
                    st[i-1] = ''
                if i != len(st)-1 and st[i+1] == ' ':
                    st[i+1] = ''
        st = ''.join(st)
        st = re.sub('[{[]', '(', st)
        st = re.sub('[]}]', ')', st)
        st = re.sub('[;]', ',', st)
        compares.append(st)

    if compares[0] == compares[1]:
        print(f'Data Set {tc}: equal')
    else:
        print(f'Data Set {tc}: not equal')

    if tc != t:
        print()
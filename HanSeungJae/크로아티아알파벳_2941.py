import sys
input = sys.stdin.readline

croatiaList = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0

st = input().strip()

for i in range(len(croatiaList)):
    while croatiaList[i] in st:
        st = st.replace(croatiaList[i], ' ', 1)
        cnt += 1

st = st.replace(' ', '')
cnt += len(st)

print(cnt)
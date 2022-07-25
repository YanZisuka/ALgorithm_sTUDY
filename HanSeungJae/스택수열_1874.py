import sys
input = lambda: sys.stdin.readline().strip()


n = int(input())
st = []
ans = []
is_st_serial = True
cur_item = 1

for i in range(n):
    num = int(input())
    while cur_item <= num:
        st.append(cur_item)
        ans.append('+')
        cur_item += 1

    if st[-1] == num:
        st.pop()
        ans.append('-')
    else:
        print('NO')
        is_st_serial = False
        break

if is_st_serial:
    for i in ans: print(i)
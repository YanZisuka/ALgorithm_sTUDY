def solution(n, k, cmd):
    answer = ['O'] * n
    stack = []
    m = len(cmd)
    now = k
    dl = {i: [i-1, i+1] for i in range(n)}
    dl[0][0] = None
    dl[n-1][1] = None

    for i in range(m):
        st = cmd[i].split()
        if len(st) > 1:
            st, num = st
            num = int(num)
            if st == 'U':
                for _ in range(num):
                    now = dl[now][0]

            elif st == 'D':
                for _ in range(num):
                    now = dl[now][1]
        else:
            st = st[0]
            if st == 'C':
                answer[now] = 'X'
                prev, next = dl[now]
                stack.append((prev, now, next))
                
                if next == None:
                    now = dl[now][0]
                else:
                    now = dl[now][1]

                if prev == None:
                    dl[next][0] = None
                elif next == None:
                    dl[prev][1] = None
                else:
                    dl[prev][1] = next
                    dl[next][0] = prev


            elif st == 'Z':
                prev, restored_now, next = stack.pop()
                answer[restored_now] = 'O'

                if prev == None:
                    dl[next][0] = restored_now
                elif next == None:
                    dl[prev][1] = restored_now
                else:
                    dl[next][0] = restored_now
                    dl[prev][1] = restored_now

    return "".join(answer)
import sys
input = sys.stdin.readline

S, E, Q = input().split()
S = int(S[:2]) * 60 + int(S[3:])
E = int(E[:2]) * 60 + int(E[3:])
Q = int(Q[:2]) * 60 + int(Q[3:])
enter_ids = set()
exit_ids = set()
cnt = 0

while True:
    try:
        time, id = input().split()
        time = int(time[:2]) * 60 + int(time[3:])

        if time <= S:
            enter_ids.add(id)

        if E <= time <= Q:
            exit_ids.add(id)

    except:
        for _ in range(len(enter_ids)):
            id = enter_ids.pop()
            if id in exit_ids:
                cnt += 1
        print(cnt)
        break

solution.py
2022-05-07 18:59:38
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
from collections import deque
from copy import deepcopy

def get_shift_row(rc):
    last_row = rc.pop()
    n_rc = []
    n_rc.append(last_row)
    n_rc.extend(rc)
    return n_rc

def get_rotate(rc):
    standard = min((len(rc) // 2), (len(rc[0]) // 2))
    temp = [0] * standard

    # 윗 부분
    for row in range(standard):
        temp[row] = deepcopy.rc[row][-1 - row]
        for col in range(-2 - row, -1 + row, -1):
            rc[row][col + 1] = deepcopy.rc[row][col]

    # 왼쪽 부분
    for col in range(standard):
        for row in range(1 + col, len(rc) - col):
            rc[row - 1][col] = deepcopy.rc[row][col]

    # 아랫 부분
    for row in range(-1, len(rc) - standard, -1):
        for col in range(1 + row, len(rc) - row):
            rc[row][col - 1] = deepcopy.rc[row][col]

    # 오른쪽 부분
    for col in range(len(rc[0]), len(rc[0]) - standard, -1):
        rc[len(rc[0]) - col][col] = deepcopy.temp[len(rc[0]) - col]
        for row in range(len(rc) - (len(rc[0]) - col) - 1, len(rc) - (len(rc[0]) - col) + 1, -1):
            rc[row - 1][col] = deepcopy.rc[row][col]

    return rc


def solution(rc, operations):

    for op in operations:
        if op == "Rotate":
            rc = get_rotate(rc)
        else:
            rc = get_shift_row(rc)

    answer = rc
    return answer

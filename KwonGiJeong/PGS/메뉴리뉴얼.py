from itertools import combinations
from collections import Counter

answer = []


def make_n(order, n):
    order_list = list(order)
    sorted_order_list = sorted(order_list)
    n_orders = list(combinations(sorted_order_list, n))
    return Counter(n_orders)


def solution(orders, course):
    for cnt in course:
        cnt_table = Counter({})
        for order in orders:
            cnt_table += make_n(order, cnt)

        max_orders = []
        max_cnt = 2

        for order, cnt in cnt_table.items():
            if cnt > max_cnt:
                max_orders.clear()
                max_orders.append(order)
                max_cnt = cnt
            elif cnt == max_cnt:
                max_orders.append(order)

        for max_order in max_orders:
            max_order_str = ''.join(max_order)
            answer.append(max_order_str)

        sorted_answer = sorted(answer)

    return sorted_answer

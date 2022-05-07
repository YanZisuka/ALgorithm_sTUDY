from collections import deque

def solution(queue1, queue2):
    sum_q1, sum_q2 = sum(queue1), sum(queue2)
    target = (sum_q1 + sum_q2) // 2
    q1 = deque(queue1)
    q2 = deque(queue2)
    cnt = 0

    while True:
        if cnt > 300000 * 2:
            cnt = -1
            break
        if sum_q1 == target:
            break

        if sum_q1 > target:
            tmp = q1.popleft()
            sum_q1 -= tmp
            q2.append(tmp)
            sum_q2 += tmp
        elif sum_q2 > target:
            tmp = q2.popleft()
            sum_q2 -= tmp
            q1.append(tmp)
            sum_q1 += tmp

        cnt += 1

    return cnt



print(solution([3, 2, 7, 2], [4, 6, 5, 1]))  # 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))  # 7
print(solution([1, 1], [1, 5]))  # -1

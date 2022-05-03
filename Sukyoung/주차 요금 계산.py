from math import ceil

def solution(fees, records):

    def calculate():  # 주차 요금 계산
        result = 0
        parking_time = 0
        for t in range(len(parking_dict[p]) // 2):
            parking_time += parking_dict[p][2 * t + 1] - parking_dict[p][2 * t]

        if parking_time > fees[0]:  # 기본 시간 초과한 경우
            result += fees[1] + (ceil((parking_time - fees[0]) / fees[2]) * fees[3])
        else:  # 초과 X
            result += fees[1]

        return result

    answer = []
    parking_list = []
    parking_dict = {}

    for r in records:
        time, car, park = r.split()
        h, m = time.split(':')
        minute = (int(h) * 60) + int(m)
        parking_list.append([car, minute])
    parking_list.sort()

    for parking in parking_list:

        if parking[0] in parking_dict:
            parking_dict[parking[0]].append(parking[1])
        else:
            parking_dict[parking[0]] = [parking[1]]

    for p in parking_dict:

        if len(parking_dict[p]) % 2 == 0:
            answer.append(calculate())
        else:  # 나간 기록이 없는 경우 23:59에 나간것으로 계산
            parking_dict[p].append(1439)
            answer.append(calculate())

    return answer
from datetime import datetime


def solution(fees, records):
    minimum_time, minimum_rate, unit_time, unit_rate = fees[0], fees[1], fees[2], fees[3]
    entry_log = {}
    parking_duration = {}
    fee_per_car = {}
    for record in records:
        time, plate_number, direction = map(str, record.split(' '))
        if plate_number not in entry_log:
            parking_duration[plate_number] = datetime.strptime('0', '%H')
            fee_per_car[plate_number] = 0
            entry_log[plate_number] = [time]
        else:
            entry_log[plate_number].append(time)

    for car in entry_log:  # 입차만 했을 경우 출차시간 23:59 설정
        if len(entry_log[car]) % 2 == 1:
            entry_log[car].append('23:59')

    for car in entry_log:  # 데이트 타임으로 변경
        for i in range(0, len(entry_log[car]), 2):
            in_time = datetime.strptime(entry_log[car][i], '%H:%M')
            out_time = datetime.strptime(entry_log[car][i + 1], '%H:%M')
            duration = out_time - in_time
            parking_duration[car] += duration

    for car in parking_duration:  # 분으로 변환
        parking_duration[car] = (parking_duration[car].hour * 60) + parking_duration[car].minute
        if parking_duration[car] == 0:
            fee_per_car[car] = 0
        elif parking_duration[car] <= minimum_time:
            fee_per_car[car] = minimum_rate
        elif parking_duration[car] > minimum_time and (parking_duration[car] - minimum_time) % unit_time == 0:
            fee_per_car[car] = minimum_rate + (((parking_duration[car] - minimum_time) // unit_time) * unit_rate)
        else:
            fee_per_car[car] = minimum_rate + (((parking_duration[car] - minimum_time) // unit_time) * unit_rate) + unit_rate
    answer = []
    fee_per_car = sorted(fee_per_car.items())
    for car in fee_per_car:
        answer.append(car[1])
    return answer


# print(solution([180, 5000, 10, 600],
#          ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
#           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

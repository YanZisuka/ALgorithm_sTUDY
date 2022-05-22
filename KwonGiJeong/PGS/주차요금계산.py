from datetime import datetime


def solution(fees, records):
    answer = []
    parking_dict, fee_dict = {}, {}

    last_out_time = datetime.strptime("23:59:00", "%H:%M:%S")

    for record in records:
        parking_time, car_number, in_out = record.split()

        parking_time = datetime.strptime(f"{parking_time}:00", "%H:%M:%S")

        if car_number not in parking_dict.keys():
            parking_dict[car_number] = []

        parking_dict[car_number].append(parking_time)

    for car_num_key in parking_dict.keys():
        park_time, car_parking_fee = 0, 0
        is_more_fee, more_fee_time = False, 0

        in_out_time_len = len(parking_dict[car_num_key])
        if in_out_time_len % 2 == 1:
            parking_dict[car_num_key].append(last_out_time)
            in_out_time_len += 1

        for i in range(in_out_time_len // 2):
            park_time += (parking_dict[car_num_key][2*(i-1)+1] -
                          parking_dict[car_num_key][2*(i-1)]).seconds // 60

        if park_time - fees[0] > 0:
            is_more_fee = True
            more_fee_time = (park_time - fees[0]) / fees[2]

            if more_fee_time != int(more_fee_time):
                more_fee_time = int(more_fee_time) + 1

        car_parking_fee = fees[1] + more_fee_time * fees[3]

        fee_dict[car_num_key] = int(car_parking_fee)

    answer = [fee[1] for fee in sorted(fee_dict.items(), key=lambda x: x[0])]

    return answer

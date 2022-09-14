import math

def solution(fees, records):
    answer = []
    preprocess = []
    parkings = {}
    times = {}
    
    for i in range(len(records)):
        time, car, status = records[i].split()
        hh, mm = map(int, time.split(':'))
        time = hh * 60 + mm
        
        if status == 'IN':
            parkings[car] = time
            if not times.get(car):
                times[car] = 0
        elif status == 'OUT':
            times[car] += time - parkings[car]
            parkings[car] = 'done'
    
    for i in range(len(records)):
        time, car, status = records[i].split()
        if parkings[car] != 'done':
            time = 23 * 60 + 59
            times[car] += time - parkings[car]
            parkings[car] = 'done'
    
    for key, value in times.items():
        fee = fees[1]
        if value > fees[0]:
            value = math.ceil((value - fees[0]) / fees[2])
            fee += value * fees[3]
        preprocess.append([key, fee])
    
    preprocess.sort()
    
    for fee_info in preprocess:
        answer.append(fee_info[1])
        
    return answer
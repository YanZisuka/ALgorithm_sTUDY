import math

def solution(fees, records):
    answer = []
    tmp = []
    parkings = {}
    times = {}
    
    for i in range(len(records)):
        time, carNum, status = records[i].split()
        hh, mm = map(int, time.split(':'))
        time = hh * 60 + mm
        
        if status == 'IN':
            parkings[carNum] = time
            if not times.get(carNum):
                times[carNum] = 0
        elif status == 'OUT':
            times[carNum] += time - parkings[carNum]
            parkings[carNum] = 'c'
    
    for i in range(len(records)):
        time, carNum, status = records[i].split()
        if parkings[carNum] != 'c':
            time = 23 * 60 + 59
            times[carNum] += time - parkings[carNum]
            parkings[carNum] = 'c'
    
    for key, value in times.items():
        fee = fees[1]
        if value > fees[0]:
            value = math.ceil((value - fees[0]) / fees[2])
            fee += value * fees[3]
        tmp.append([key, fee])
    
    tmp.sort()
    
    for feeInfo in tmp:
        answer.append(feeInfo[1])
        
    return answer
import math
def hourTominute(time):
    hour, minute= time.split(":")
    return 60*int(hour) + int(minute)

def solution(fees, records):
    default_time, default_fee, unit_time, unit_fee = fees
    midnight_time =hourTominute("23:59")
    record_dict ={} # 출입시간, 누적시간
    answer = []
    for record in records:
        _time, _car_number, _move = record.split()
        
        if _move == "IN":
            if _car_number in record_dict.keys():
                record_dict[_car_number][0] = hourTominute(_time)
            else :
                record_dict[_car_number] = [hourTominute(_time), 0] 
        elif _move == "OUT":
            parking_time = hourTominute(_time) - record_dict[_car_number][0]
            record_dict[_car_number][0] = None 
            record_dict[_car_number][1] +=  parking_time
    
    
    for _car_number in sorted(record_dict.keys()):
        _enter_time, _parking_time = record_dict[_car_number]
        _fee = 0
        if _enter_time != None :
            _parking_time += (midnight_time - _enter_time)
        if _parking_time <= default_time:
            _fee = default_fee
        else :
            _fee = default_fee + math.ceil((_parking_time - default_time) \
                                           / unit_time)*unit_fee
        answer.append(_fee)
            
    return answer
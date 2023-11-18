from collections import defaultdict

def solution(fees, records):
    answer = []
    default_time, default_fee, per_time, per_fee = fees
    
    record_dict = defaultdict(int) # 차량 입차 시간
    answer_dict = defaultdict(int) # 누적 주차 시간
    for record in records:
        time, car, inNout = record.split(' ')
        time = str2time(time)
        if inNout=='IN':
            record_dict[car] = time
        else:
            answer_dict[car] += time-record_dict[car]
            record_dict[car] = -1
            
    final = str2time("23:59")
    for car in record_dict.keys():
        if record_dict[car]>-1:
            answer_dict[car] += final-record_dict[car]
            
    for answer_car in sorted((answer_dict.keys())):
        answer_time=int(answer_dict[answer_car])
        time2pay = answer_time-default_time
        per = 0
        if time2pay>0:
            per = time2pay//per_time + int(time2pay%per_time>0)
        fee = default_fee + per*per_fee
        answer.append(fee)
        
    return answer

def str2time(time):
    h,m = map(int, time.split(':'))
    return h*60+m

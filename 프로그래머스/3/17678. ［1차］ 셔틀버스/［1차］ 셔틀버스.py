# ref. https://mjmjmj98.tistory.com/121

def solution(n, t, m, timetable):
    # n:운행 횟수, t:운행 간격, m:탑승가능인원
    # answer = ''
    timeTB = sorted([time2val(t) for t in timetable])
    busTB = list(range(0,n*t,t))
    
    i=0 # 다음에 버스에 오를 크루의 인덱스
    for bus in busTB:
        cnt = 0
        while cnt<m and i<len(timeTB) and timeTB[i]<=bus:
            i+=1
            cnt+=1
        if cnt<m: answer = bus
        else: answer = timeTB[i-1]-1
        
    return val2time(answer)

def time2val(str_time):
    h,m = map(int,str_time.split(':'))
    return 60*(h-9)+m

def val2time(int_time):
    h = int_time//60 + 9
    m = int_time%60
    return f'{h:02d}:{m:02d}'
    
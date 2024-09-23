def solution(play_time, adv_time, logs):
    play_time = time2int(play_time)
    ad_time = time2int(adv_time)
    
    # 시청자 수 변화 기록 배열
    dp = [0] * (play_time + 1)
    
    # 로그의 시청 시작과 끝 시간 기록
    for log in logs:
        start, end = map(time2int, log.split('-'))
        dp[start] += 1
        dp[end] -= 1
    
    # dp 배열을 누적 시청자 수로 변환
    for i in range(1, play_time):
        dp[i] += dp[i-1]
    
    # dp 배열을 누적 시청 시간으로 변환
    for i in range(1, play_time):
        dp[i] += dp[i-1]
    
    # 광고를 삽입했을 때의 최대 시청 시간 구하기
    max_time = 0
    best_start = 0
    for start in range(play_time - ad_time + 1):
        end = start + ad_time
        # 광고 구간의 시청 시간 합을 구함
        current_time = dp[end-1] - (dp[start-1] if start > 0 else 0)
        if current_time > max_time:
            max_time = current_time
            best_start = start
    
    return int2time(best_start)

# 시간을 초로 변환
def time2int(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s

# 초를 다시 시간 형식으로 변환
def int2time(time):
    h = time // 3600
    m = (time % 3600) // 60
    s = time % 60
    return f"{h:02}:{m:02}:{s:02}"

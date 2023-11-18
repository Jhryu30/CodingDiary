def solution(land):
    answer = 0
    
    dp = land[0]
    for i in range(1,len(land)):
        dp_new = [max(dp[1:]), max([dp[0]]+dp[2:]), max(dp[:2]+[dp[3]]), max(dp[:-1])]
        dp = [dp_new[col]+land[i][col] for col in range(4)]
        
    answer = max(dp)
    
    return answer
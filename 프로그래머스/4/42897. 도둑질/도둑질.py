def solution(money):
    answer = 0
    N = len(money)
    dp1 = [0 for _ in range(N)]; dp1[0] = dp1[1] = money[0] # 첫 번째 집 턀음
    dp2 = [0 for _ in range(N)]; dp2[1] = money[1] # 첫 번째 집 안 털음
    
    for i in range(2,N-1):
        dp1[i] = max(dp1[i-1],dp1[i-2]+money[i])
        dp2[i] = max(dp2[i-1],dp2[i-2]+money[i])
        
    dp1[N-1] = max(dp1[-2],dp1[0]) # 마지막 집 안 털음
    dp2[N-1] = max(dp2[-3]+money[-1],dp2[-2]) # 마지막 집 털 수 있음
    
    answer = max(dp1[-1],dp2[-1])
    return answer
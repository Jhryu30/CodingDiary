def solution(e, starts):
    answer = []
    dp = [0 for _ in range(e+2)]
    for i in range(1, e+1):
        for j in range(i, e+1, i):
            dp[j] += 1

            
    history = [0 for _ in range(e+1)]
    max_idx = e
    history[e] = e
    for idx in range(e,min(starts)-1,-1):
        if dp[idx]>=dp[max_idx]:
            max_idx = idx
        history[idx] = max_idx
        
    answer = [history[s] for s in starts]
        
    return answer
def solution(triangle):
    answer = 0
    N = len(triangle)
    dp = triangle[0]
    
    for depth in range(1,N):
        tri = triangle[depth]
        old = dp
        dp = [old[0]+tri[0]] + [max(old[j-1],dp[j])+tri[j] for j in range(1,depth)] + [old[-1]+tri[-1]]
        
    answer = max(dp)
    return answer
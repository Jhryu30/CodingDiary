def solution(m, n, puddles):
    answer = 0
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    # initial dp
    dp[0] = [1 for _ in range(m)]
    for r in range(n):
        dp[r][0] = 1
        
    puddles = [[p1-1,p0-1] for p0,p1 in puddles]
    for p_r,p_c in puddles:
        if p_r==0:
            for c in range(p_c,m):
                dp[0][c] = 0
        if p_c==0:
            for r in range(p_r,n):
                dp[r][0] = 0
                
    # update dp
    for i in range(1,n):
        for j in range(1,m):
            up = dp[i-1][j] if [i-1,j] not in puddles else 0
            left = dp[i][j-1] if [i,j-1] not in puddles else 0            
            dp[i][j] = (up+left)%1000000007
    # print(*dp, sep='\n')
    answer = dp[-1][-1]
    return answer
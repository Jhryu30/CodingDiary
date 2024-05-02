def solution(n):
    if n%2:
        return 0
    
    dp = [0 for _ in range(n//2)]
    dp[0] = 3
    for i in range(1,n//2):
        dp[i] = (2*(sum(dp[:i])+1)+dp[i-1])%1000000007
    answer = dp[-1]
    
    return answer
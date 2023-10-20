def solution(sticker):
    answer = 0
    N = len(sticker)
    if N<6:
        if N<=2:
            return max(sticker)
        elif N==3:
            return max(sticker[0]+sticker[2], sticker[1])
        elif N==4:
            return max(sticker[0]+sticker[2], sticker[1]+sticker[3])
        else:
            cand = [[0,2],[0,3],[1,3],[1,4],[2,4]]
            cand_res = [sticker[c[0]]+sticker[c[1]] for c in cand]
            return max(cand_res)
        
    dp = [0 for _ in range(N)]
    dp[0] = sticker[0]; dp[1]=sticker[1]; dp[2]=sticker[2]; dp[3]=sticker[3]
    
    dp1 = dp[:] # use sticker[0], no sticker[-1]
    dp1[2] += sticker[0]; dp1[3] += max(sticker[0],dp1[1])
    dp2 = dp[:] # no sticker[0], maybe use sticker[-1]
    dp2[3] += dp2[1]
    
    for i in range(4,N-1):
        dp1[i] = max(dp1[i-3:i-1])+sticker[i]
        dp2[i] = max(dp2[i-3:i-1])+sticker[i]
    dp2[-1] = max(dp2[1:-2])+sticker[-1]
    result = [dp1[-2],dp1[-3], dp2[-1],dp2[-2]]
    answer = max(result)

    return answer
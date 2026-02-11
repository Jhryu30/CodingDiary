def solution(e, starts):
    divisor = [0 for i in range(e+1)]
    for i in range(2,e+1):
        for j in range(1,min(e//i+1, i)):
            divisor[i*j] += 2
    for i in range(1,int(e**(1/2))+1):
        divisor[i**2] += 1
        
    dp = {}
    min_s = min(starts)
    maximum_c = 0
    num = 0
    for s in range(e, min_s-1, -1):
        c = divisor[s]
        if maximum_c <= c:
            maximum_c = c
            num = s
        
        dp[s] = num
    
    return [dp[s] for s in starts]
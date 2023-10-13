def solution(sequence):
    answer = 0
    dp1=sequence[:]; dp2=[-s for s in sequence]
    
    for i in range(1,len(sequence)):
        if i%2==0:
            dp1[i] = max(sequence[i],dp1[i-1]+sequence[i])
            dp2[i] = max(-sequence[i],dp2[i-1]-sequence[i])
        else:
            dp1[i] = max(-sequence[i],dp1[i-1]-sequence[i])
            dp2[i] = max(sequence[i],dp2[i-1]+sequence[i])
            
    answer = max(dp1+dp2)
    return answer
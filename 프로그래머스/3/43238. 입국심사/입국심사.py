def solution(n, times):
    answer = 0
    M = len(times)
    
    answer_min = 0; answer_max = n*times[0]
    
    while answer_min<answer_max:
        answer_mid = (answer_min+answer_max)//2
        wait = [answer_mid//t for t in times]
        
        if sum(wait)<n:
            answer_min = answer_mid+1
        elif sum(wait)>=n:
            answer_max = answer_mid
    
    return answer_min


def solution(triangle):
    answer = 0
    
    N = len(triangle)
    dp_old = [0 for _ in range(N)]
    dp_old[0] = triangle[0][0]
    
    depth = 0
    while depth<N-1:
        depth += 1
        current = triangle[depth]
        dp_new = [0 for _ in range(N)]
        
        for i in range(depth+1):
            if i==0 :
                dp_new[i] = dp_old[i]+current[i]
            elif i==depth:
                dp_new[i] = dp_old[i-1]+current[i]
            else:
                dp_new[i] = max(dp_old[i-1],dp_old[i])+current[i]
            if dp_new[i]>answer:
                answer = dp_new[i]
                
        dp_old = dp_new
                
    return answer
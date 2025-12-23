def solution(diffs, times, limit):
    answer = 0
    
    def lvl_solver(diffs,times,lvl):
        result = 0
        for diff,time in zip(diffs,times):
            if diff<=lvl:
                result += time
            else:
                result += (diff-lvl)*(prev_time+time)+time
            prev_time = time
        return result
    
    
    left,right = 0,10**15
    mid = (left+right)//2
    while left<mid<right:
        mid_time = lvl_solver(diffs,times,mid)
        if mid_time>limit:
            left = mid
        else:
            right = mid
        mid = (left+right)//2
    answer = mid+1
                
    return answer
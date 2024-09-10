from heapq import heappop, heappush

def solution(scores):
    answer = 1
    wanho = scores[0]
    w = sum(wanho)
    
    heap = []
    for x,y in scores[1:]:
        if x+y>w:
            heappush(heap,(-x-y,x,y))
            
        if wanho[0] < x and wanho[1] < y:
            return -1
            
    if heap:
        prev_k,x,y = heappop(heap)
        left, right = (x,y), (x,y)
        answer += 1
    
    while heap:
        k,x,y = heappop(heap)
        if k == prev_k:
            answer += 1
        else:
            if (x<=left[0] and y>=left[1]):
                left = (x,y)
                answer += 1
            elif (x>=right[0] and y<=right[1]):
                right = (x,y)
                answer += 1
    
    
    return answer
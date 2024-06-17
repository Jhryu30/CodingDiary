from heapq import heappop, heappush, heappop

def solution(a):
    answer = 0
    
    heap = []
    for i,v in enumerate(a):
        heappush(heap,(v,i))
    
    min_v,min_i = heappop(heap)
    left_i, right_i = min_i, min_i
    while heap:
        v,i = heappop(heap)
        if min_i<i and left_i<i:
            left_i = i
            answer += 1
        elif min_i>i and right_i>i:
            right_i = i
            answer += 1
            
    return answer+1
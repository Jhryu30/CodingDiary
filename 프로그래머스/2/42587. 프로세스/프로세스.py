from heapq import heapify, heappop, heappush
from collections import deque

def solution(priorities, location):
    answer = 0
    N = len(priorities)
    queue = deque([(idx,priorities[idx]) for idx in range(N)])
    process_rank = []
    for rank in priorities:
        heappush(process_rank,-rank)
    
    rank = -heappop(process_rank)
    while queue:
        idx,process = queue.popleft()
        if not process==rank:
            queue.append((idx,process))
        else:
            answer += 1
            if idx==location:
                return answer
            rank = -heappop(process_rank)
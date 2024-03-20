from heapq import heappush, heappop

def solution(jobs):
    answer = 0
    jobs.sort()
    heap = []
    idx,N = 0,len(jobs)
    
    time = 0
    while idx<N or heap:
        while idx<N and jobs[idx][0]<=time:
            called,duration = jobs[idx]
            wait = duration-called # +time
            heappush(heap,(duration,called))
            idx +=1
            
        if heap:
            duration,called = heappop(heap)
            answer += time+duration-called
            time += duration
        else:
            time += 1
        
    return answer//N
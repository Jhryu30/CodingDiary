from collections import deque

def solution(jobs):
    answer = 0
    
    jobs.sort(key=lambda x:[x[1],x[0]])
    jobs = deque(jobs)
    
    t=0
    while jobs:
        job = jobs.pop()
        if job[0]<=t:
            t+=job[0]
        else:
            jobs.append(job)
            jobs.sort()
            
    return answer
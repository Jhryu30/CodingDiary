from heapq import heappush, heappop

def solution(lines):
    answer = 0

    # preprocess
    queue = []
    for line in lines:
        _, end, t = line.split(' ')
        h,m,s = map(float,end.split(':'))

        dt = float(t[:-1])
        end = 3600*h + 60*m + s
        start = max(0,end-dt+0.001)
        queue.append((start,end))
        
    # find max traffic
    for start,end in queue:
        cnt = 0
        for s,e in queue:
            if s<end+1 and end<=e:
                cnt += 1
        answer = max(cnt,answer)
        
    return answer
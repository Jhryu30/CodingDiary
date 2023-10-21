import heapq

def solution(jobs):
    answer = 0
    N = len(jobs)
    
    start, t, done = -1,0,0
    # start:이전 작업 시작 | t:현재 시점 | done:완료된 작업 수
    heap = []
    
    while done<N:
        # 현재 시점에 처리 가능한 일들을 heap에 추가
        for j in jobs:
            if start<j[0] and j[0]<=t:
                heapq.heappush(heap, [j[1],j[0]]) #[소요시간,요청시간]
        if heap:
            # 지금 처리할 만한 일(=작업 소요시간 가장 적은 일)
            j = heapq.heappop(heap)
            start = t
            t += j[0] # 작업 진행(시간 소모)
            answer += t-j[1]
            done += 1
        else:
            t += 1
    
    return answer//N
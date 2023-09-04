from collections import deque

def solution(progresses, speeds):
    answer = []
    
    if len(progresses)==0:
        return answer
    
    # 각 작업이 배포될 수 있는 일 수를 queue에 저장
    queue = deque()
    for i in range(len(progresses)):
        left = 100-progresses[i]
        if left%speeds[i]==0:
            queue.append(left//speeds[i])
        else:
            queue.append(left//speeds[i]+1)
            
    # 이전 작업의 배포 일과 비교해서 answer에 새로/함께 배포할지 결정하여 저장
    old_start = queue.popleft()
    answer.append(1)
    
    while queue:
        new_start = queue.popleft()
        if old_start<new_start:
            answer.append(1)
            old_start = new_start
        else:
            answer[-1] += 1
            
    
    return answer
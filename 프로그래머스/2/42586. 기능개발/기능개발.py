def solution(progresses, speeds):
    answer = [0]
    N = len(progresses)
    left = [100-progresses[i] for i in range(N)]
    release = [left[i]//speeds[i]+int(left[i]%speeds[i]>0) for i in range(N)]
    
    day = release[0]
    for i in range(N):
        if release[i]<=day:
            answer[-1]+=1
        else:
            day = release[i]
            answer.append(1)
            
    return answer
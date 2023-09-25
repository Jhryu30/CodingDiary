def solution(n, lost, reserve):
    reserve2 = sorted([r for r in reserve if r not in lost])
    lost2 = sorted([l for l in lost if l not in reserve])
    answer = n-len(lost2)
    
    for l in lost2:
        if len(reserve2)==0:
            return answer
        try:
            reserve2.remove(l-1)
            answer += 1
        except:
            try:
                reserve2.remove(l+1)
                answer +=1
            except:
                pass
    
    return answer
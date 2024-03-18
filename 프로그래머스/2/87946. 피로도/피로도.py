from itertools import permutations

def solution(k, dungeons):
    answer = -1
    # 최소 필요 피로도, 소모 피로도
    
    N = len(dungeons)
    
    for explore in permutations(dungeons, N):
        current, flag = k, 1
        for i,(necessary,used) in enumerate(explore):
            if current>=necessary:
                current -= used
            else:
                answer = max(i,answer)
                flag = 0
                break
        if flag:
            answer = N
                
    return answer
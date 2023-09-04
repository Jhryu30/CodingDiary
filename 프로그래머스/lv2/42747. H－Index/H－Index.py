def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for idx in range(len(citations)):
        if idx < citations[idx]:
            answer += 1
        else:
            break
    
    return answer
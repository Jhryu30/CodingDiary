def solution(numbers):
    answer = [0 for _ in range(len(numbers))]
    
    previous = []
    for idx,num in enumerate(numbers):
        while previous and num>previous[-1][1]:
            prev_idx, prev_num = previous.pop()
            answer[prev_idx] = num
        previous.append([idx,num])
        
    while previous:
        prev_idx, prev_num = previous.pop()
        answer[prev_idx] = -1
        
    return answer
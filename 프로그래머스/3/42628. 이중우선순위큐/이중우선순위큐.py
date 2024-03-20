def solution(operations):
    answer = []
    
    queue = []
    for oper in operations:
        cmd,num = oper.split(' ')
        if cmd=='I':
            queue.append(int(num))
        elif queue:
            if num[0]=='-':
                min_val = min(queue)
                queue.remove(min_val)
            else:
                max_val = max(queue)
                queue.remove(max_val)
                
    answer = [max(queue),min(queue)] if queue else [0,0]
    
    return answer
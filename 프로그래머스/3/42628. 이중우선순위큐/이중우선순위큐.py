from collections import deque

def solution(operations):
    answer = []
    
    queue = []
    for oper in operations:
        cmd,num = oper.split(' ')
        num = int(num)
        if cmd=='I':
            queue.append(num)
            queue.sort()
        else:
            if num>0:
                queue = queue[:-1]
            else:
                if len(queue)>0:
                    queue = queue[1:]
                else:
                    pass
    if len(queue)>0:
        answer = [queue[-1], queue[0]]
    else:
        answer = [0,0]
    
    return answer
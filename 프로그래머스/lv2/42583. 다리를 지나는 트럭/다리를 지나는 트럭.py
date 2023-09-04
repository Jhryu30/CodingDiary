from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    on_bridge = deque(tuple([0 for _ in range(bridge_length-1)] +[truck_weights[0]]))
    waiting = deque(tuple(truck_weights[1:]))
    
    sum_bridge = sum(on_bridge)
    sum_waiting = sum(waiting)
    
    while sum_bridge+sum_waiting > 0:
        answer += 1
        sum_bridge -= on_bridge.popleft()
        wait = waiting.popleft() if len(waiting)>0 else 0
        
        if sum_bridge+wait <= weight:
            on_bridge.append(wait)
            sum_bridge += wait
            sum_waiting -= wait
        else:
            on_bridge.append(0)
            waiting.appendleft(wait)
            
    return answer
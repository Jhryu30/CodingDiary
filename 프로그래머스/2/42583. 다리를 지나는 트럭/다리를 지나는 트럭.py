from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge,bridge_weight = deque([0 for _ in range(bridge_length)]),0
    truck_weights = deque(truck_weights)
    
    truck = truck_weights.popleft()
    while truck or bridge_weight:
        previous = bridge.popleft()
        bridge_weight -= previous
        if truck and bridge_weight+truck<=weight:
            bridge.append(truck)
            bridge_weight += truck
            truck = truck_weights.popleft() if truck_weights else 0
        else:
            bridge.append(0)
        answer += 1
        
    return answer
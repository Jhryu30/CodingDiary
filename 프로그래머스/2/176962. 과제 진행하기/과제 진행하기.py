from heapq import heapify, heappush, heappop

def solution(plans):
    answer = []
    
    # plans.sort(key=lambda x: (int(x[1][:2]) * 60 + int(x[1][3:]), x[0]))
    
    heap = []
    for name, start, playtime in plans:
        h, m = map(int, start.split(":"))
        start = 60 * h + m
        heappush(heap, (start, int(playtime), name))
    
    previous = []
    current_start, current_playtime, current_name = heappop(heap)
    
    while heap or previous:
        if heap:
            next_start, next_playtime, next_name = heappop(heap)
            
            if current_start + current_playtime > next_start:
                previous.append((current_start + current_playtime - next_start, current_name))
                current_start, current_playtime, current_name = next_start, next_playtime, next_name
            else:
                answer.append(current_name)
                current_start = current_start + current_playtime
                
                while previous and current_start + previous[-1][0] <= next_start:
                    current_playtime, current_name = previous.pop()
                    answer.append(current_name)
                    current_start += current_playtime
                
                if previous:
                    current_playtime, current_name = previous.pop()
                    heappush(heap, (next_start, next_playtime, next_name))
                else:
                    current_start, current_playtime, current_name = next_start, next_playtime, next_name
                    if not heap:
                        answer.append(current_name)
        else:
            answer.append(current_name)
            while previous:
                current_playtime, current_name = previous.pop()
                answer.append(current_name)
    
    return answer
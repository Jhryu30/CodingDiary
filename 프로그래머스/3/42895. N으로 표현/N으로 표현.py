from collections import deque, defaultdict

def solution(N, number):
    answer = 0
    
    depth_dict = defaultdict(list) # depth:[numbers]
    visited = defaultdict(int)
    depth_dict[1].append(N)
    if N==number:
        return 1
    
    for depth in range(2,9):
        # case1. NNN꼴
        new_v = int(str(N)*depth)
        depth_dict[depth].append(new_v)
        visited[new_v] = 1
        if new_v==number:
            return depth
        
        # case2. 이전 depth에서 나온 값들 간의 사칙연산으로 표현
        for depth1 in range(1,depth//2+1):
            depth2 = depth-depth1
            
            for a in depth_dict[depth1]:
                for b in depth_dict[depth2]:
                    if a==0 or b==0:
                        continue
                    for op in '+-*/':
                        new_v = int(eval(str(a)+op+str(b)))
                        if new_v<=32000 and not visited[new_v]:
                            depth_dict[depth].append(new_v)
                            visited[new_v] = 1
                            if new_v==number:
                                return depth
                    for op in '-/':
                        new_v = int(eval(str(b)+op+str(a)))
                        if new_v<=32000 and not visited[new_v]:
                            depth_dict[depth].append(new_v)
                            visited[new_v] = 1
                            if new_v==number:
                                return depth
                
    
    return -1
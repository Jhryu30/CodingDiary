from heapq import heappush, heappop
import copy

def solution(name):
    N = len(name)
    letter_dict = {l: min(i, 26 - i) for i, l in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    name = list(name)
    
    queue = [] # (cnt, idx, name)
    heappush(queue, (letter_dict[name[0]], 0, ['A'] + name[1:]))
    want = ['A' for _ in range(N)]
    visited = set()
    
    def search(cnt1, idx1, name1):
        nonlocal queue
        idx1 %= N
        cnt1 += letter_dict[name1[idx1]] + 1
        new_name1 = copy.deepcopy(name1)
        new_name1[idx1] = 'A'
        
        state = (idx1, tuple(new_name1)) 
        
        if state not in visited: 
            visited.add(state) 
            heappush(queue, (cnt1, idx1, new_name1))
    
    while queue:
        cnt0, idx0, name0 = heappop(queue)
        if name0 == want:
            return cnt0
        search(cnt0, idx0 + 1, name0)
        search(cnt0, idx0 - 1, name0)
    
    return -1 
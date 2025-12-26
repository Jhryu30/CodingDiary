from heapq import heappush, heappop

def solution(alp, cop, problems):
    problems.sort()
    max_alp, max_cop = max([prob[0] for prob in problems]), max([prob[1] for prob in problems])
    
    visited = [[0 for _ in range(300)] for _ in range(300)]
    actions = [(0,0,1,0,1), (0,0,0,1,1)]
    for prob in problems:
        actions.append(prob)
    
    queue = [(0,alp,cop)]
    while queue:
        time,alg,cog = heappop(queue)
        # print(alg,cog)
        if visited[alg][cog]:
            continue
        visited[alg][cog] = 1
        if alg>=max_alp and cog>=max_cop:
            return time
        for a,c,da,dc,dt in actions:
            if alg>=a and cog>=c:
                new_alg,new_cog,new_time = alg+da, cog+dc, time+dt
                heappush(queue,(new_time,min(max_alp,new_alg), min(max_cop,new_cog)))
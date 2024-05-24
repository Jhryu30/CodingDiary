from collections import defaultdict, deque

def solution(edges):
    '''
    1. 중심 node 찾기 : 나가는 edge 2개 이상, 들어오는 edge 없음
    2. 8자 : 나가는 edge 2개. 한 번 쑥 돌기
    3. 도넛, 막대 : 쑥 돌아보고 visited node 만나는지 여부로 판단
    '''
    answer = []
    
    graph = defaultdict(list)
    count_in = defaultdict(int)
    for a,b in edges:
        graph[a].append(b)
        count_in[a]; count_in[b] += 1
        
    nodes = list(count_in.keys())
    visited = [0 for _ in range(max(nodes)+1)]
    for v in nodes:
        if count_in[v]==0 and len(graph[v])>=2:
            start = v
            visited[start] = 1
            break
    
    doughnut,stick,eight = 0,0,0
    
    for v in nodes:
        if len(graph[v])==2 and not v==start:
            eight += 1
            queue = deque([v])
            visited[v] = 1
            while queue:
                v = queue.popleft()
                for new_v in graph[v]:
                    if not visited[new_v]:
                        queue.append(new_v)
                        visited[new_v] = 1
        
        
    for v in graph[start]:
        if not visited[v]:
            queue = deque([v])
            visited[v] = 1
            flag = 1
            ori_v = v
            while queue:
                v = queue.popleft()
                for new_v in graph[v]:
                    if not visited[new_v]:
                        queue.append(new_v)
                        visited[new_v] = 1
                    else:
                        flag = 0
            if flag:
                stick += 1
            else:
                doughnut += 1
    
    answer = [start,doughnut,stick,eight]
                
    return answer
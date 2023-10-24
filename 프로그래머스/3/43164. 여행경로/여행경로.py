from collections import defaultdict, deque

def solution(tickets):
    answer = ['ICN']
    N = len(tickets)
    ticket_dict = defaultdict(list)
    dest_dict = defaultdict(list)
    
    for i,(t0,t1) in enumerate(tickets):
        ticket_dict[t0].append([t1,i])
        ticket_dict[t1]
        dest_dict[t1].append(t0); dest_dict[t0]
    final_destination = 0
    for t in ticket_dict.keys():
        ticket_dict[t].sort()
        if not ticket_dict[t]:
            final_destination = t
    
    def dfs(graph,v,i,visited):
        nonlocal final_destination
        
        for new_v,new_i in graph[v]:
            if not visited[new_i]:
                if new_v==final_destination and not visited[i]==N-1:
                    print(new_v,new_i)
                    pass
                else:
                    visited[new_i] = visited[i]+1
                    dfs(graph,new_v,new_i,visited)
                    pass
    
    v='ICN'; i=ticket_dict['ICN'][0][1]
    visited = [0 for _ in range(N)]
    dfs(ticket_dict, v, i , visited)
    
    answer_idx = sorted(range(N), key=lambda x:visited[x])
    answer += [tickets[i][1] for i in answer_idx]
    print(visited)
    print([tickets[i] for i in answer_idx])
    return answer
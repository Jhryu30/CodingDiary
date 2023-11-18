def solution(dirs):
    graph = {(r,c):[0,0,0,0] for r in range(-5,6) for c in range(-5,6)} # u,d,r,l
    dir_dict = {'U':[0,[0,1]],'D':[1,[0,-1]],'R':[2,[1,0]],'L':[3,[-1,0]]}
    dir_opp = {'U':'D', 'R':'L', 'D':'U', 'L':'R'}
    
    answer = 0
    v = (0,0)
    for direction in dirs:
        x,y = v
        d, [dx,dy] = dir_dict[direction]
        d_, [dx_,dy_] = dir_dict[dir_opp[direction]]
        
        new_x,new_y = x+dx, y+dy
        new_v = new_x,new_y
        if new_x<-5 or new_y<-5 or new_x>5 or new_y>5:
            continue
        if not graph[new_v][d]:
            answer += 1
        graph[new_v][d]=1; graph[v][d_]=1
        v=new_v
        
    return answer
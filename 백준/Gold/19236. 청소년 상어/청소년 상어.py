import sys
import copy

input = sys.stdin.readline

direction = {1:(-1,0),2:(-1,-1),3:(0,-1),4:(1,-1),5:(1,0),6:(1,1),7:(0,1),8:(-1,1)}
graph = [[0 for _ in range(4)] for _ in range(4)]
fish = {n:[[-1,-1],-1] for n in range(17)}

for i in range(4):
  line = list(map(int,input().split()))
  for j in range(4):
    a,b = line[2*j:2*j+2]
    graph[i][j] = [a,b]
    fish[a] = [[i,j],b]

def move_fish(graph,fish,depth=0):
  for n in range(1,17):
    loc,dir = fish[n]
    if dir==-1:
      continue
    x,y = loc
    while True:
      dir = dir%8; dir = 8 if dir==0 else dir
      dx,dy = direction[dir]
      new_x = x+dx; new_y = y+dy
      if new_x<0 or new_y<0 or new_x>=4 or new_y>=4 or graph[new_x][new_y][0]==-1:
        # 경계 밖으로 나가거나, 상어가 있으면
        dir += 1
        continue

      new_n,new_dir = graph[new_x][new_y]
      graph[new_x][new_y] = [n,dir]; fish[n] = [[new_x,new_y],dir]
      graph[x][y] = [new_n,new_dir]; fish[new_n] = [[x,y],new_dir]
      break

  return graph, fish

def move_shark(graph,fish,shark,step,score,depth=0):
  graph = copy.deepcopy(graph); fish = copy.deepcopy(fish)
  loc,dir = shark
  if dir<0:
    return False, 0,0,0,score
  x,y = loc; dx,dy = direction[dir]
  new_x = x+step*dx; new_y = y+step*dy

  if new_x<0 or new_y<0 or new_x>=4 or new_y>=4 or graph[new_x][new_y]==0 :
    # 경계 밖으로 나가거나, 물고기가 없으면
    return False, 0, 0, 0, score


  new_n,new_dir = graph[new_x][new_y]
  graph[new_x][new_y] = [-1,new_dir]; shark = [[new_x,new_y],new_dir]
  graph[x][y] = [0,-1]; fish[new_n] = [[-1,-1],-1]
  return True, graph, fish, shark, score+new_n

def dfs(graph,fish,shark,score=0,depth=0):
  global max_score
  graph = copy.deepcopy(graph); fish = copy.deepcopy(fish)
  graph_f, fish_f = move_fish(graph,fish,depth)
  graph_f = copy.deepcopy(graph_f); fish_f = copy.deepcopy(fish_f)
  for step in range(1,4):
    moved, graph_s, fish_s, shark_s, score_s = move_shark(graph_f,fish_f,shark,step,score,depth)
    if moved:
      max_score = max(max_score, score_s)
      dfs(graph_s,fish_s,shark_s,score_s,depth+1)
  return

# initial value
x,y = 0,0
n,dir = graph[x][y]
graph[x][y] =  [-1,dir]; shark = [[x,y],dir]
fish[n] = [[-1,-1],-1]

score,max_score = n,n
dfs(graph,fish,shark,score,depth=0)
print(max_score)